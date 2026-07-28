# Handoff — enclosure and structural transformation

**Written:** 2026-07-28.
**Purpose:** start a focused research conversation on the manufacturing extension, separate
from the site-reorganisation work happening in the main thread.

This is a *research* handoff, not a migration one. The question is whether the three-sector
extension yields publishable results — possibly a separate paper — not whether code moves
correctly.

---

## 0. Why this is its own thread

The main thread is Phase 3 of a repo reorganisation (`REORGANIZATION_PROPOSAL.md`), whose
operating rule is explicit: **move prose, do not author economics.** Everything below
requires deriving new results, so it does not belong there.

The immediately useful things already exist: a tested implementation, verified numbers, and
one genuinely new result. What is missing is the welfare apparatus — and one conceptual
problem that has to be settled before any welfare claim can be made (§3).

---

## 1. Where the material lives

| What | Where |
|---|---|
| Canonical draft (334 lines + notes) | `enclosure_book/notebooks/enclosure_manuf.md` |
| Superseded shorter draft (216 lines) | `enclosure_book/notebooks/Manufactures and Structural Transformation.md` |
| Original notebook (defines its own `LM`, `mpla`, `mplm`, `pl`) | `enclosure_book/notebooks/enclosure_manuf.ipynb` |
| **Tested implementation** | `open-enclose.github.io/enclose/manufacturing.py` |
| Tests | `open-enclose.github.io/tests/test_manufacturing.py` |
| Site page written from all of the above | `open-enclose.github.io/content/03-manufacturing.md` |
| Appendix equations (35)–(36) | `enclosure_book/docs/online_appendix.md` §6.4 |

The appendix's note that this extension is "sketched but not fully developed" is **out of
date** — it was written without reference to the 334-line draft.

`enclose.manufacturing` reproduces the draft's headline example exactly (19.7% → 67.6%,
wage 1.14 → 0.79), so the port is faithful and can be trusted as a starting point.

---

## 2. What is established

### The model

Labor moves until $w = p\,MPL_m = MPL_e = APL_u$. Given $l_m$, the within-agriculture
allocation is the benchmark reaction function scaled by $(1-l_m)$ — eq. (36). The
manufacturing margin is

$$
\underbrace{p \beta \bar k^{1-\beta}}_{C_m}\, l_m^{-(1-\beta)}
=
\underbrace{\bar t^{1-\alpha}\left(1+(\Lambda_\mu-1)t_e\right)^{1-\alpha}}_{C_a}\,
(1-l_m)^{-(1-\alpha)}
\qquad\Longleftrightarrow\qquad
\frac{l_m^{1-\beta}}{(1-l_m)^{1-\alpha}} = \frac{C_m}{C_a}
$$

### Three results, all verified numerically

1. **Unique equilibrium.** $MPL_m$ falls in $l_m$, $MPL_a$ rises; exactly one sign change on
   $(0,1)$ across parameter sweeps. Justifies a bracketed solver.
2. **No closed form except at $\beta=\alpha$**, where it collapses to $l_m = R/(1+R)$,
   $R = (C_m/C_a)^{1/(1-\alpha)}$. Agrees with the numerical solve to 12 significant
   figures — used as a test oracle.
3. **Enclosure's effect on structural transformation reverses at $\theta_H$.** This is the
   new one. $\partial l_m/\partial t_e$ has the sign of $(\Lambda_\mu-1)$, and
   $\Lambda_\mu = 1$ exactly at $\theta_H^\mu = \frac{1}{\alpha}-\mu\frac{1-\alpha}{\alpha}$.
   Below it enclosure releases labor to manufacturing; above it labor is pulled back; at it
   enclosure moves no labor at all. The knife-edge is exact.

(1) and (2) were anticipated in the draft's prose; (3) was not.

### Why (3) matters

The draft's headline example — 20% → 70% manufacturing under full enclosure — sits at
$\theta=1$, $\alpha=0.4$, hence $\theta_H = 2.5$ and $\Lambda = 0.22$: **squarely on the
low-TFP branch.** So the familiar "enclosure freed labor for industry" account is a claim
about that branch specifically. Where enclosure delivers the *largest* productivity gain, it
is *least* likely to release labor.

Sharper still: at $\theta=1$ the planner's $\Lambda_o = 1$, so the planner's $l_m$ is
**completely unmoved** by enclosure, while the decentralized economy shifts half its
workforce. The entire reallocation is the commons distortion, not productivity.

---

## 3. The blocking problem — resolve this first

**At $t_e=0$ the $\Lambda_\mu$ term in $C_a$ vanishes, so the private and planner
agricultural labor-demand curves coincide exactly.** (Visible as overlapping curves in the
left panel of `Figures/manufacturing_equilibrium.png`.)

That looks wrong. With all land in an open-access commons, labor should enter until
$APL_u = w$; a planner would set $MPL_u = w$; those differ by a factor of $\alpha$. The
draft's planner expression is the marginal product in the *enclosed* sector

$$
\bar t^{1-\alpha}\left(\frac{t_e}{l_e^*(t_e)}\right)^{1-\alpha}
= \bar t^{1-\alpha}(1-t_e+\Lambda_o t_e)^{1-\alpha}\left(\frac{1}{1-l_m}\right)^{1-\alpha}
$$

evaluated where **no enclosed sector exists**. As $t_e\to0$, $t_e/l_e^* \to 1/\Lambda$, so
the limit is not obviously the right benchmark.

**Why this blocks everything downstream:** every welfare comparison in §4 is against the
$\mu=1$ curve. If that curve is not the planner's allocation at low $t_e$, the comparisons
are wrong exactly where the interesting example lives.

First task: derive the planner's three-sector first-order conditions directly from the
objective in `enclosure_manuf.md` §"Socially optimal enclosure with manufacturing" —

$$
\max_{t_e,\,l_e,\,l_m}\ \theta F(T_e,L_e) + F(\bar T-T_e,\ \bar L-L_m-L_e)
+ p\,G(\bar K,L_m) - c\,T_e
$$

— and check whether the resulting $l_m$ agrees with `mpl_a(..., mu=1)`. If it does not,
`manufacturing.py` needs a separate planner path, and `content/03-manufacturing.md` §4 needs
correcting.

---

## 4. Questions worth pursuing, once §3 is settled

**a. Is enclosure at $\theta=1$ unambiguously welfare-reducing?** Conjecture: yes. No TFP
gain, wages fall 1.14 → 0.79, and the inter-sectoral allocation moves *away* from the
planner's. If it holds, it is a clean statement — enclosure that is privately profitable and
socially destructive on *every* margin at once, without needing any productivity story.

**b. Does enclosure raise or lower measured aggregate TFP?** This is the bridge to the
literature. Aggregate output per worker can rise purely because labor moved from a
low-average-product commons to manufacturing, with no technology change anywhere. Worth
computing measured TFP explicitly and asking whether enclosure's apparent TFP gain is
mostly this composition effect.

**c. What is the equilibrium $t_e$?** The whole page currently treats $t_e$ as exogenous.
Closing the loop — deriving decentralized enclosure *with* a manufacturing outside option —
is what turns this from an extension into a paper. Expect the enclosure loci to shift, since
the outside option changes the commons' value.

**d. Does $\tau$ interact with the reversal?** $\tau$ enters the enclosure condition, not the
labor-allocation condition, so it should not move $\theta_H$ — but it changes which $t_e$ is
reached, and hence where on the reversal curve the economy sits.

**e. Endogenise $p$.** Currently exogenous. A general-equilibrium price could overturn the
partial-equilibrium comparative statics.

---

## 5. Relation to the existing literature

The papers cited in the main paper model misallocation as **within-agriculture skill
sorting** — high-ability households cannot get enough land, so exogenous "enclosure" or
titling raises aggregate TFP by reallocating land toward them.

Our model has **homogeneous labor**, so it cannot speak to that channel at all. But it has a
different one those papers do not: the **commons as a labor sponge**. Enclosure raises
measured aggregate TFP by expelling labor into manufacturing, not by making anyone more
productive — and per result (3), that channel *reverses sign* at $\theta_H$.

That is a sharper and more falsifiable claim than "enclosure raises TFP", and it is the most
promising differentiator for a separate paper. It also suggests an empirical prediction: the
labor-release effect of enclosure should be **strongest where the productivity gain is
smallest**, which is the opposite of what a pure technology story predicts.

---

## 6. Practical notes

- Work in `open-enclose.github.io`; `pip install -e ".[dev]"`, then `pytest tests/`.
- `enclose.model` is numpy-only; `enclose.manufacturing` adds scipy (`brentq`).
- **`labor_share` takes `mu` and threads it through** — there is a test guarding that,
  because an earlier bug in `tepvt_g` accepted `mu` and silently ignored it. Watch for that
  failure mode in anything new.
- `enclose.symbolic` derives every benchmark locus from its objective and checks the numeric
  layer against it. Nothing equivalent exists for the manufacturing case yet; adding it
  would be the natural way to verify §3's derivation.
- The two drafts (§1) should be reconciled before any write-up. `enclosure_manuf.md` is
  canonical.
- `plotmpts` / `figures.labor_misallocation` still carries `TODO: not yet working for
  mu != 0`. If a welfare figure is needed for $\mu>0$, that must be fixed first.
