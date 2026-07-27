# Generate Figures/trajectories.png -- parameter-change trajectories figure
# for the final RESTUD revision (editor item iii / Referee 2's request).
# Matthew J. Baker and Jonathan Conning
#
# Two panels in (theta, ln lbar) space, alpha = 2/3, c/A = 1, reusing the loci
# of Figure 5 (comparison.png, Model_Construction.ipynb cell / enclose.py):
#   (a) movements in fundamentals (lbar, c/A) against fixed benchmark loci
#       (mu = tau = 0): Weitzman-Samuelson point, Boserup arrow (smooth),
#       barbed-wire/cheap-titling arrow (tipping point).
#   (b) movements in institutions (economy point fixed): the global-games
#       locus lbar_gg^d drawn for tau = 0 and tau = 1, Marx/Brenner point,
#       theta_H^mu arrow (eq. 26), De Janvry point.
#
# Design spec: paper/final_revisions.md section 1.4 (iii).
#
# Key geometric fact stated in the figure note: every locus has the form
# ln lbar = (1/alpha) ln(c/A) + g(theta), so shocks to c or A shift all loci
# by the same vertical distance -- equivalent to moving the economy's point
# vertically against fixed loci. Hence panel (a) draws lbar and c/A shocks
# as vertical arrows on one fixed canvas.
#
# tau-modified enclosure condition (eqs. 23/27 in main.tex): the encloser's
# payoff per unit land is r^e - tau*r^c - c. Along the labor reaction
# function l_e^0(t_e), r^e - tau*r^c =
# (1-alpha)*A*lbar^alpha * (theta*Lam^alpha - tau) * (1+(Lam-1)t_e)^(-alpha)
# with Lam = (alpha*theta)^(1/(1-alpha)). Integrating over t_e in [0,1]
# (Laplacian beliefs) gives the global-games risk-dominance locus
#   lbar_gg^d(tau) = [ (c/A)(1-Lam) / ((theta*Lam^alpha - tau)(1-alpha*theta)) ]^(1/alpha)
# which reduces to eq. (17) at tau = 0 (theta*Lam^alpha = Lam/alpha).
# For tau = 1 the locus diverges at theta*Lam^alpha = 1, i.e. at
# theta_tau = alpha^(-alpha) (~1.31 for alpha = 2/3): with full compensation
# no population density makes a raid profitable below theta_tau.
#
# Run:  python generate_trajectories_figure.py
# Output: <repo>/paper/Figures/trajectories.png

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Parameters -- same as all figures in the paper
ALP = 2/3          # labor share alpha
C = 1.0            # c/A
CV = 1/ALP         # theta_H = 1/alpha = 1.5
THETA_TAU = ALP**(-ALP)   # asymptote of the tau=1 gg locus (~1.310)

YLIM = (-1.8, 4.4)
XLIM = (0.74, 2.34)
HATCH_CAP = 3.6    # top cap for the low-TFP over-enclosure hatch


def lam0(th):
    '''Lambda at mu=0:  (alpha*theta)^(1/(1-alpha))'''
    return (ALP*th)**(1/(1-ALP))


def ln_l01(th):
    '''First-best no-enclosure locus, eq. (6)'''
    lamO = th**(1/(1-ALP))
    return (1/ALP)*np.log(C/((lamO - 1)*(1-ALP)))


def ln_l11(th):
    '''First-best full-enclosure locus, eq. (7):  lbar_1^1 = Lam_o * lbar_0^1'''
    return ln_l01(th) + (1/(1-ALP))*np.log(th)


def ln_ld0(th):
    '''Decentralized r(0)=c locus, eq. (14)'''
    return (1/ALP)*np.log(ALP*C/((1-ALP)*lam0(th)))


def ln_ld1(th):
    '''Decentralized r(1)=c locus, eq. (15)'''
    return (1/ALP)*np.log(C/(th*(1-ALP)))


def ln_gg(th, tau=0.0):
    '''Global-games risk-dominance locus, eq. (17), extended by compensation
       parameter tau (eq. 23): E[r^e - tau*r^c - c] = 0 over t_e in [0,1].
       Defined for theta < theta_H and theta*Lam^alpha > tau; +inf elsewhere.'''
    lam = lam0(th)
    margin = th*lam**ALP - tau      # = Lam/alpha - tau
    out = np.full_like(np.asarray(th, dtype=float), np.inf)
    ok = (margin > 0) & (th < CV)
    with np.errstate(divide='ignore', invalid='ignore'):
        out[ok] = (1/ALP)*np.log(C*(1-lam[ok])/(margin[ok]*(1-ALP*th[ok])))
    return out


def ln_ls(th):
    '''Second-best full-vs-none locus (low-TFP side), eq. (18)'''
    return (1/ALP)*np.log(C/(th - 1))


def ln_lc0(th):
    '''Second-best no-enclosure locus (high-TFP side), eq. (19)'''
    lam = lam0(th)
    return (1/ALP)*np.log(ALP*C/((lam*(1+ALP) - ALP)*(1-ALP)))


def base_panel(ax):
    '''Draw the Figure 5 (comparison.png) canvas: first-best band, second-best
       loci (blue dashed), decentralized loci (red), over/under-enclosure
       hatching, dotted verticals at theta=1 and theta_H. Returns the low-TFP
       theta grid so callers can overlay the gg locus in their own style.'''
    th_lo = np.linspace(0.82, CV-1e-6, 500)     # low-TFP side (gg domain)
    th_hi = np.linspace(CV, 2.1, 500)           # high-TFP side
    th_fb = np.linspace(1.1, 2.1, 500)          # first-best loci
    th_s = np.linspace(1.02, CV, 500)           # second-best lbar^s

    # First-best loci and partial-enclosure band
    ax.plot(th_fb, ln_l01(th_fb), color='blue', alpha=.54)
    ax.plot(th_fb, ln_l11(th_fb), color='blue', alpha=.54)
    ax.fill_between(th_fb, ln_l01(th_fb), ln_l11(th_fb), alpha=.05, color='C0')

    # Second-best loci (blue dashed); lbar_1^s coincides with lbar_1^d,
    # offset slightly so both are visible (as in comparison.png)
    ax.plot(th_s, ln_ls(th_s), color='blue', linestyle='dashed', linewidth=2)
    ax.plot(th_hi, ln_lc0(th_hi), color='blue', linestyle='dashed')
    ax.plot(th_hi, ln_ld1(th_hi)-.017, color='blue', linestyle='dashed')

    # Decentralized loci on the high-TFP side (red)
    ax.plot(th_hi, ln_ld0(th_hi), color='red')
    ax.plot(th_hi, ln_ld1(th_hi), color='red', linewidth=2)

    # Over-enclosure hatching (low-TFP): above lbar_gg^d, below lbar^s
    # (lbar^s -> +inf as theta -> 1+, so cap the hatch near the canvas top)
    upper = np.where(th_lo > 1.001, ln_ls(np.maximum(th_lo, 1.001)), np.inf)
    upper = np.minimum(upper, HATCH_CAP)
    ax.fill_between(th_lo, ln_gg(th_lo), upper, alpha=.75, hatch='.',
                    color='none', linewidth=0.0, edgecolor='red')

    # Under-enclosure hatching (high-TFP): coordination failure band
    # (lbar_0^s to lbar_0^d, fine dots) and partial band (lbar_0^d to lbar_1^d)
    ax.fill_between(th_hi, ln_lc0(th_hi), ln_ld0(th_hi), alpha=.5, hatch='...',
                    color='none', linewidth=0.0, edgecolor='blue')
    ax.fill_between(th_hi, ln_ld0(th_hi), ln_ld1(th_hi), alpha=.5, hatch='..',
                    color='none', linewidth=0.0, edgecolor='blue')

    # Dotted verticals at theta = 1 and theta_H = 1/alpha
    ax.axvline(CV, ymax=.95, linestyle=':', color='black')
    ax.axvline(1, ymax=.95, linestyle=':', color='black')
    ax.text(1, YLIM[0]+.06, r'$1$', fontsize=14, ha='center')
    ax.text(CV, YLIM[0]+.06, r'$\theta_H=\frac{1}{\alpha}$', fontsize=14,
            ha='center')

    # Right-edge and left-edge locus labels (as in comparison.png)
    ep = 2.115
    ax.text(ep, ln_l01(2.1), r'$\bar l^1_0$', fontsize=13)
    ax.text(ep, ln_l11(2.1)+.05, r'$\bar l^1_1$', fontsize=13)
    ax.text(ep, ln_lc0(2.1), r'$\bar l^s_0$', fontsize=13)
    ax.text(ep, ln_ld1(2.1)-.07, r'$\bar l^s_1, \bar l^d_1$', fontsize=13)
    ax.text(ep, ln_ld0(2.1)+.16, r'$\bar l^d_0$', fontsize=13)
    ax.text(1.075, 4.05, r'$\bar l^s$', fontsize=13)

    # Axes cosmetics (house style)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    xlbl = ax.set_xlabel(r'$\theta$', fontsize=18)
    xpos = list(xlbl.get_position())
    ax.xaxis.set_label_coords(xpos[0]+.44, xpos[1]-.02)
    ax.set_ylabel(r'$\ln(\overline{l})$', fontsize=16)

    return th_lo


ARROW = dict(arrowstyle='-|>', linewidth=2.2, color='black',
             shrinkA=0, shrinkB=0, mutation_scale=18)
WBOX = dict(facecolor='white', edgecolor='none', alpha=0.85, pad=1.2)
ARROW_LEN = 1.6   # common length of the two panel-(a) shock arrows


def panel_a(ax):
    '''Movements in fundamentals against loci fixed at mu = tau = 0.'''
    th_lo = base_panel(ax)
    # benchmark gg locus, dashed red as in Figure 4
    ax.plot(th_lo, ln_gg(th_lo), color='red', linestyle='dashed', linewidth=2)
    ax.text(th_lo[0]-.055, ln_gg(th_lo[:1])[0]+.04, r'$\bar l^d_{gg}$',
            fontsize=13)
    ax.set_title(r'(a) Fundamentals: shocks to $\bar l$ and $c/A$'
                 r'  (loci fixed, $\mu=\tau=0$)', fontsize=13.5)

    # -- Weitzman-Samuelson: theta = 1, below lbar_gg^d: commons persists ----
    ax.scatter(1.0, 0.9, s=45, color='black', zorder=5, clip_on=False)
    ax.text(1.0, 0.55, 'Weitzman–Samuelson', fontsize=11, ha='center',
            va='top', bbox=WBOX)

    # -- Boserup: same-length vertical arrow at theta ~ 2 crossing lbar_0^d --
    x = 2.0
    y0 = -1.30
    ax.annotate('', xy=(x, y0+ARROW_LEN), xytext=(x, y0), arrowprops=ARROW)
    ax.text(x+.03, y0+.12, 'Boserup', fontsize=11, ha='left', bbox=WBOX)
    cross = ln_ld0(np.array([x]))[0]
    ax.scatter(x, cross, s=48, facecolor='white', edgecolor='black',
               zorder=6, linewidth=1.4)
    ax.text(x-.05, cross+.04, 'smooth expansion', fontsize=10, ha='right',
            style='italic', bbox=WBOX)

    # -- Barbed wire / cheap titling: same-length arrow crossing lbar_gg^d --
    x = 1.2
    y0 = 0.70
    ax.annotate('', xy=(x, y0+ARROW_LEN), xytext=(x, y0), arrowprops=ARROW)
    ax.text(x-.035, 1.45, 'Barbed wire /\ncheap titling', fontsize=11,
            ha='right', va='center', bbox=WBOX)
    cross = ln_gg(np.array([x]))[0]
    ax.scatter(x, cross, s=48, facecolor='white', edgecolor='black',
               zorder=6, linewidth=1.4)
    ax.text(x+.045, cross-.06, 'tipping point', fontsize=10, ha='left',
            style='italic', bbox=WBOX)

    # Region orientation labels
    ax.text(0.86, 3.0, 'over-enclosure', fontsize=10, style='italic',
            color='darkred', rotation=-22, bbox=WBOX)
    ax.text(1.72, 0.12, 'under-enclosure', fontsize=10, style='italic',
            color='darkblue', rotation=-13, bbox=WBOX)

    # Equivalence note: c/A shocks are vertical movements
    ax.text(XLIM[0]+.04, YLIM[0]+.32,
            r'Vertical arrows: rise in $\bar l$ or equal-sized fall in $c/A$'
            '\n' r'(all loci scale as $(c/A)^{1/\alpha}$).',
            fontsize=9.5, style='italic', va='bottom')


def panel_b(ax):
    '''Movements in institutions (tau, mu) with the economy's point fixed.'''
    th_lo = base_panel(ax)
    ax.set_title(r'(b) Institutions: shifts in $\tau$ and $\mu$'
                 r'  (economy fixed)', fontsize=13.5)

    # -- lbar_gg^d drawn twice: tau = 0 (solid red) and tau = 1 (darkred) ----
    ax.plot(th_lo, ln_gg(th_lo), color='red', linewidth=2)
    ax.text(0.775, 2.55, r'$\bar l^d_{gg}(\tau\!=\!0)$', fontsize=12,
            ha='left', bbox=WBOX)

    th_tau = np.linspace(THETA_TAU+1e-4, CV-1e-6, 800)
    ax.plot(th_tau, ln_gg(th_tau, tau=1.0), color='darkred', linewidth=2)
    ax.text(1.515, 2.85, r'$\bar l^d_{gg}(\tau\!=\!1)$', fontsize=13,
            ha='left', color='darkred', bbox=WBOX)
    # the tau=1 locus diverges at theta_tau = alpha^(-alpha) ~ 1.31: with
    # full compensation no density triggers a raid to the left of it
    ax.text(1.245, 3.82, r'$\to\infty$: no raid pays for'
            '\n' r'$\theta<\alpha^{-\alpha}$ when $\tau=1$',
            fontsize=9, ha='center', va='center', style='italic',
            color='darkred', bbox=WBOX)

    # arrow showing the locus sweeping down as tau falls from 1 to 0
    x = 1.46
    ax.annotate('', xy=(x, ln_gg(np.array([x]))[0]+.12),
                xytext=(x, ln_gg(np.array([x]), tau=1.0)[0]-.10),
                arrowprops=dict(arrowstyle='-|>', linewidth=2.0,
                                color='darkred', mutation_scale=16))
    ax.text(x+.02, 2.15, r'$\tau: 1\to 0$', fontsize=11, ha='left',
            color='darkred', bbox=WBOX)

    # -- Marx / Brenner: between the two gg loci at theta ~ 1.1 --------------
    ax.scatter(1.1, 2.7, s=45, color='black', zorder=6)
    ax.text(1.085, 2.98, 'Marx / Brenner', fontsize=11, ha='right', bbox=WBOX)

    # -- mu arrow: theta_H^mu pushed left from 1/alpha (mu=0) to 1 (mu=1) ----
    ax.annotate('', xy=(1.04, -1.35), xytext=(1.49, -1.35),
                arrowprops=ARROW)
    ax.text(1.265, -1.12,
            r'$\mu\!\uparrow$:  $\theta_H^\mu=\frac{1}{\alpha}'
            r'-\mu\frac{1-\alpha}{\alpha}\;\to\;1$',
            fontsize=11, ha='center', bbox=WBOX)

    # -- De Janvry: high-theta under-enclosure band (lbar_0^s, lbar_0^d) -----
    ax.scatter(1.9, -0.24, s=45, color='black', zorder=6)
    ax.text(1.9, -0.62, 'De Janvry', fontsize=11, ha='center', bbox=WBOX)


def sanity_checks():
    '''Verify the tau = 1 gg locus lies above the tau = 0 locus wherever it
       is defined (compensation reduces enclosure returns, so full enclosure
       requires higher density), and check formulas against notebook values.'''
    th = np.linspace(THETA_TAU+1e-3, CV-1e-3, 400)
    g0, g1 = ln_gg(th, tau=0.0), ln_gg(th, tau=1.0)
    assert np.all(g1 > g0), 'tau=1 gg locus must lie above tau=0 locus'
    print(f'OK: gg(tau=1) > gg(tau=0) on ({th[0]:.3f}, {th[-1]:.3f}); '
          f'min gap {np.min(g1-g0):.3f} (ln units)')
    print(f'OK: tau=1 asymptote at theta = alpha^-alpha = {THETA_TAU:.4f}')

    # cross-check tau=0 gg against Model_Construction.ipynb formula (eq. 17)
    lamg = lam0(th)
    nb = (1/ALP)*np.log(ALP*C/(1-ALP*th)*(1-lamg)/lamg)
    assert np.allclose(g0, nb), 'gg(tau=0) must match notebook formula'
    print('OK: gg(tau=0) matches the comparison.png / eq. (17) formula')

    # annotation points sit in the intended regions
    ws_gg = ln_gg(np.array([1.0]))[0]
    assert 0.9 < ws_gg, 'W-S point must lie below lbar_gg^d'
    mx_gg = ln_gg(np.array([1.1]))[0]
    mx_ls = ln_ls(np.array([1.1]))[0]
    assert mx_gg < 2.7 < mx_ls, \
        'Marx/Brenner point must sit between lbar_gg^d(tau=0) and lbar^s'
    dj_lo, dj_hi = ln_lc0(np.array([1.9]))[0], ln_ld0(np.array([1.9]))[0]
    assert dj_lo < -0.24 < dj_hi, \
        'De Janvry point must sit between lbar_0^s and lbar_0^d'
    print('OK: annotation points verified against their loci')


def main():
    sanity_checks()
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(16, 7))
    panel_a(axa)
    panel_b(axb)
    fig.tight_layout(w_pad=3.0)

    # No .resolve(): keep the repo's Y:\ drive mapping rather than following
    # it to a machine-specific path.
    outdir = Path(__file__).absolute().parents[1] / 'paper' / 'Figures'
    outdir.mkdir(parents=True, exist_ok=True)
    outfile = outdir / 'trajectories.png'
    fig.savefig(outfile, dpi=120, facecolor='white')
    print(f'Saved {outfile}')


if __name__ == '__main__':
    main()
