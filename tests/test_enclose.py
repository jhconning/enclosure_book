"""Tests pinning down the density convention in enclose.py.

Everything here is about one thing: every function takes `lbar`, population
density $\\bar l = \\bar L / \\bar T$, as in the paper. `plotreq` previously had a
single parameter named `tlbar` that it passed positionally to `req` (whose slot
meant L/T) and to `weq` (whose slot meant T/L), so one of the two curves was
inverted whenever the density was not 1. `test_plotreq_curves_share_one_density`
is the direct guard against that returning.
"""
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pytest

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'notebooks'))
import enclose as e  # noqa: E402

TE_ALL = np.array([0.0, 0.2, 0.5, 0.8, 1.0])
# the MPT/MPL identities are stated at interior t_e: at t_e=0 both l_e and t_e
# are zero and the per-unit marginal products are 0/0, though req/weq stay finite
TE = np.array([0.2, 0.4, 0.5, 0.8, 0.99])
TH, ALP = 2.2, 0.5


@pytest.mark.parametrize('mu', [0.0, 0.5, 1.0])
@pytest.mark.parametrize('lbar', [0.25, 1.0, 4.0])
def test_rental_equals_marginal_product_of_land(mu, lbar):
    """r(t_e) is MPT evaluated at the equilibrium labor allocation l_e(t_e).

    This is the invariant the two reciprocal conventions were hiding: `req` and
    `mpt` used to be parameterized by reciprocals of each other, so this held
    only at density 1.
    """
    le = e.le(TE, TH, ALP, mu)
    np.testing.assert_allclose(
        e.req(TE, TH, ALP, lbar, mu),
        e.mpt(TE, le, ALP, TH, lbar),
    )


@pytest.mark.parametrize('lbar', [0.25, 1.0, 4.0])
def test_wage_equals_marginal_product_of_labor_at_mu_zero(lbar):
    """At mu=0 the wage is MPL on enclosed land at l_e(t_e)."""
    le = e.le(TE, TH, ALP, mu=0.0)
    np.testing.assert_allclose(
        e.weq(TE, TH, ALP, lbar, mu=0.0),
        e.mple(TE, le, ALP, TH, lbar),
    )


@pytest.mark.parametrize('mu', [0.25, 0.5, 1.0])
def test_wage_scales_by_security_wedge_for_positive_mu(mu):
    """For mu>0, weq is that same marginal product scaled by (1-mu+alp*mu)."""
    le = e.le(TE, TH, ALP, mu)
    np.testing.assert_allclose(
        e.weq(TE, TH, ALP, 2.0, mu) * (1 - mu + ALP * mu),
        e.mple(TE, le, ALP, TH, 2.0),
    )


def test_factor_prices_scale_with_density_in_opposite_directions():
    """r ~ lbar**alp, w ~ lbar**(alp-1). Denser labor raises rents, cuts wages."""
    k = 4.0
    np.testing.assert_allclose(
        e.req(TE_ALL, TH, ALP, lbar=k), k**ALP * e.req(TE_ALL, TH, ALP, lbar=1.0)
    )
    np.testing.assert_allclose(
        e.weq(TE_ALL, TH, ALP, lbar=k), k**(ALP - 1) * e.weq(TE_ALL, TH, ALP, lbar=1.0)
    )


def test_mpl_is_alpha_times_apl():
    """Cobb-Douglas identity, and a check that both carry the same density term."""
    np.testing.assert_allclose(
        e.mple(0.4, 0.6, ALP, TH, lbar=3.0),
        ALP * e.aple(0.4, 0.6, ALP, TH, lbar=3.0),
    )


def test_plotreq_curves_share_one_density():
    """The regression guard: plotreq's r and w must be drawn at the same lbar.

    Under the old code the single parameter landed in req's L/T slot and weq's
    T/L slot, so the w curve here would come out as weq(..., 1/lbar).
    """
    lbar = 0.16   # the value enclosure_model.ipynb uses for r_three_high
    fig, ax = plt.subplots()
    e.plotreq(th=TH, alp=ALP, lbar=lbar, c=0.5, wplot=True, ax=ax)

    curves = {line.get_label(): line for line in ax.get_lines()}
    tte = curves[r'$r$'].get_xdata()

    np.testing.assert_allclose(
        curves[r'$r$'].get_ydata(), e.req(tte, TH, ALP, lbar=lbar)
    )
    np.testing.assert_allclose(
        curves[r'$w$'].get_ydata(), e.weq(tte, TH, ALP, lbar=lbar)
    )
    plt.close(fig)


@pytest.mark.parametrize('lbar', [0.25, 1.0, 4.0])
def test_totalq_matches_closed_form_z_at_mu_one(lbar):
    """At mu=1, l_e is the first-best allocation, so totalq must equal z(t_e).

    totalq previously multiplied by th twice (once inside f's th argument and
    once again outside), giving th**2 instead of th. z() is the closed-form
    planner's output and is derived independently (it never calls f), so
    agreement here is a genuine cross-check on totalq.
    """
    np.testing.assert_allclose(
        e.totalq(TE, TH, ALP, lbar, mu=1.0),
        e.z(TE, TH, ALP, lbar),
    )


def test_r_three_high_panels_straddle_the_cost_line():
    """The three r_three_high panels are a comparative static across c=0.5.

    This is why the 0.16/0.19/0.24 values in enclosure_model.ipynb are lbar and
    not its reciprocal: read as T/L they would imply lbar=6.25 and r(0) about
    3.0, far above c, making all three panels identical in message.
    """
    c = 0.5
    r0 = [e.req(0.0, 2.2, 0.5, lbar=b) for b in (0.16, 0.19, 0.24)]
    assert r0[0] < c < r0[1] < r0[2]
