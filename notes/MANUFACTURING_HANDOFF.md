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
   new one. $\partial l_m/\partial t_e$ has the sign of $(1-\Lambda_\mu)$ — note the
   inversion, the equilibrium condition rises in $l_m$ so $l_m$ rises when $C_a$ falls —
   and
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

At $\theta=1$ the planner's $\Lambda_o = 1$, so the planner's $l_m$ is **completely
unmoved** by enclosure, while the decentralized economy shifts half its workforce. The
reallocation is the commons distortion, not productivity.

But note *where* the planner sits — see §3. It is flat at $l_m = 0.68$, which is where the
decentralized economy **ends up** under full enclosure, not where it starts. The
reallocation runs toward the optimum, not away from it. An earlier version of this note
said the opposite; that was the §3 bug.

This is a claim about the labor margin *conditional on $t_e$*, and nothing more. It does
**not** say full enclosure is first best — at $\theta \le 1$ the planner would not enclose
at any positive cost. See §4a.

---

## 3. The blocking problem — RESOLVED 2026-07-28

**Verdict: the planner's FOCs do *not* agree with `mpl_a(..., mu=1)`. The code overstated
the planner's agricultural labor demand by exactly $1/\alpha$.** Fixed in
`open-enclose.github.io`: `enclose/manufacturing.py`, `enclose/figures.py`, both test files,
`content/03-manufacturing.md`, `Figures/manufacturing_equilibrium.png`.

### The symptom

At $t_e=0$ the $\Lambda_\mu$ term in $C_a$ vanished, so the private and planner
agricultural labor-demand curves coincided exactly — the overlapping curves in the left
panel of `Figures/manufacturing_equilibrium.png`. That was wrong: with all land in an
open-access commons labor enters until $APL_u = w$, whereas a planner sets $MPL_u = w$, and
the two differ by a factor of $\alpha$.

### The cause

The draft writes the agricultural return as
$\bar t^{1-\alpha}\left(t_e/l_e^*(t_e)\right)^{1-\alpha}$. Substituting $l_e^*$ leaves a
prefactor $\alpha\theta\Lambda_\mu^{-(1-\alpha)}$, which equals **exactly 1 at $\mu=0$** —
by construction of $\Lambda$ — and so looks droppable. In general it is

$$
A_\mu = 1 - \mu(1-\alpha), \qquad A_0 = 1,\quad A_1 = \alpha
$$

$\Lambda_\mu$ carries $\mu$ into the *slope* of the agricultural allocation; $A_\mu$ carries
it into the *level*. The module kept the first and dropped the second. Every established
$\mu=0$ result — including the 19.7% → 67.6% headline and the wage fall — is untouched,
because $A_0 = 1$.

### The correct FOCs

From $\max_{t_e,l_e,l_m}\ \theta F(T_e,L_e) + F(\bar T-T_e,\ \bar L-L_m-L_e) + p\,G(\bar K,L_m) - c\,T_e$:

$$
\alpha\theta\left(\tfrac{t_e}{l_e}\right)^{1-\alpha}
= \alpha\left(\tfrac{1-t_e}{1-l_m-l_e}\right)^{1-\alpha}
\quad\Longrightarrow\quad
l_e^o = \tfrac{\Lambda_o t_e}{1+(\Lambda_o-1)t_e}(1-l_m)
$$

— eq. (36) at $\mu=1$, which was already right. Substituting back:

$$
p\,\beta\bar k^{1-\beta}l_m^{-(1-\beta)}
= \boxed{\alpha}\ \bar t^{1-\alpha}\left(1+(\Lambda_o-1)t_e\right)^{1-\alpha}(1-l_m)^{-(1-\alpha)}
$$

### How it was verified

Three independent ways, all agreeing. Sympy gives `[code]/[planner MPL_u] = 1/alpha`
symbolically. Direct Nelder–Mead maximisation of the objective over $(l_e,l_m)$ matches the
corrected formula to <1e-5 across six parameter sets and the old code not at all — 0.676 vs
0.197 at the headline parameters. And solving the decentralized equal-return system from
primitives, with no $\Lambda$ formula anywhere, matches the corrected formula for
$\mu \in \{0, 0.5, 1\}$ to 1e-9. The first two are now regression tests; reintroducing the
bug fails twelve of them.

### Two properties that now pin the level

- **$t_e=0$:** the whole economy is the commons, $\Lambda_\mu$ drops out, and the two curves
  must stand in the ratio $\alpha$ exactly.
- **$t_e=1$:** there is no commons, so $\mu$ cannot matter at all —
  $C_a = \alpha\theta\bar t^{1-\alpha}$ for every $\mu$. Equivalently, **full enclosure
  implements the planner's inter-sectoral allocation for any $\theta$** (checked at
  $\theta = 0.8, 1.0, 1.5, 2.5$). The old code made $l_m$ at $t_e=1$ depend on $\mu$ — the
  same defect from the other end, and a sharper diagnostic than the $t_e=0$ one, since it
  needs no appeal to what a planner "should" do. **Conditional on $t_e$ only** — see §4a
  for why this does not make $t_e=1$ optimal.

### What survives, what does not

- **Result (3) survives untouched.** $A_\mu$ contains neither $t_e$ nor $l_m$, so
  $\partial l_m/\partial t_e$ still takes the sign of $(1-\Lambda_\mu)$ and the knife-edge is
  still exactly $\theta_H^\mu$. The sign-reversal test now runs across $\mu$, which is what
  actually pins "level, not slope".
- **§4a is refuted** — see below.

### Still open

`enclose.symbolic` still has no manufacturing counterpart. The sympy check written for this
was throwaway; folding it into `symbolic.py` would give the three-sector case the same
derive-and-verify treatment the benchmark loci get, and is the natural guard against the
next algebra slip of this kind.

---

## 4. Questions worth pursuing, now that §3 is settled

**a. Is enclosure at $\theta=1$ unambiguously welfare-reducing? No — the conjecture was
wrong, and it was wrong because of the §3 bug.** The old reasoning was: no TFP gain, wages
fall 1.14 → 0.79, and the inter-sectoral allocation moves *away* from the planner's. The
third leg is false. The allocation moves *toward* the planner's and at $t_e=1$ reaches it
exactly. With $c=0$ total output rises 13.0% from $t_e=0$ to $t_e=1$, purely from
reallocation, with no technology change anywhere.

The wage leg also needs restating. At $t_e=0$ labor captures the whole average product of
the commons; at $t_e=1$ it is paid a marginal product. The fall from 1.14 to 0.79 is a
change in *which of the two* labor receives — a distributional fact, not a fall in anyone's
productivity. Output and labor's share move in opposite directions.

**But the answer to (a) as originally posed is still "broadly yes", by a different route —
and I initially got this wrong in the other direction.** The first correction only concerned
the labor margin, holding $t_e$ fixed. The planner also *chooses* $t_e$, and that is a
separate margin with a separate threshold. Adding it back (envelope theorem, so the labor
terms drop out):

$$
\frac{dY}{dt_e} = (1-\alpha)\,\bar t^{1-\alpha}(\Lambda_o-1)
\left(\frac{1-l_m(t_e)}{1+(\Lambda_o-1)t_e}\right)^{\alpha}
$$

— the benchmark's $z'(t_e)$ with the *agricultural* labor share in place of the whole labor
force. Manufacturing changes the level, not the sign, and the sign is that of
$(\Lambda_o - 1)$, i.e. of $(\theta - 1)$. **Note $\Lambda_o$, not $\Lambda_\mu$: this
margin turns at $\theta=1$, not at $\theta_H$.** Confusing the two is the obvious trap.

So $t_e^o = 0$ for every $c>0$ whenever $\theta \le 1$, however misallocated the
decentralized economy's labor is at $t_e=0$. **Full enclosure is first best only for
$\theta>1$ and $c$ small enough.** Verified numerically over a $(\theta, c)$ grid.

The decisive comparison at $\theta=1$, $\alpha=0.4$, $\beta=0.7$:

| | output |
|---|---:|
| decentralized, no enclosure ($\mu=0,\ t_e=0$) | 1.236 |
| decentralized, full enclosure ($\mu=0,\ t_e=1$) | 1.397 $-\ c\bar T$ |
| **regulated commons, no enclosure ($\mu=1,\ t_e=0$)** | **1.397** |

Enclosure closes the whole 0.161 gap — and so does regulating the commons, at $t_e=0$, for
no enclosure cost. **Enclosure is a second-best instrument here**: it repairs the labor
misallocation by abolishing the institution that caused it, which works, but pays $c\bar T$
for what governance delivers directly. It beats doing nothing only while $c\bar T < 0.161$,
and it never beats fixing the commons.

That is the defensible claim, and it is *not* the enclosure-friendly one: where enclosure
raises output without raising productivity, it is substituting for institutional reform, not
achieving something reform could not. It also puts the $\mu$-vs-$t_e$ trade-off — two costly
instruments aimed at one distortion — squarely on the agenda; $\tau$ belongs in that
comparison too.

One band worth knowing about: for $\theta$ slightly below 1 the commons distortion is still
large enough that full enclosure raises *decentralized* output while lowering the planner's
— down to $\theta \approx 0.73$ at these parameters. Unlike $\theta_H$ that crossover is
parameter-dependent (0.89 at $\alpha=\beta=0.5$, 0.42 at $p=2$), so it is a feature of the
example, not a result.

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

The §3 correction sharpens this rather than weakening it. The labor-sponge channel is not
just a measurement artefact to be netted out — per §4a it is a genuine output gain, since
the commons really was holding too much labor on the land. So enclosure can raise output
*through the labor margin alone*, with plot-level TFP held fixed at $\theta=1$ — exactly
the case the skill-sorting literature has no mechanism for.

The normative half is the more distinctive contribution, and it cuts the other way: that
gain is available without enclosure, by regulating the commons instead. The model therefore
delivers a **second-best** account of historical enclosure — the right frame for a
literature that has mostly asked whether enclosure raised productivity, when the sharper
question is whether it was the cheapest available fix for what was actually wrong. That also
connects the paper to the Ostrom-style evidence on commons governance in a way the
skill-sorting papers cannot.

---

## 6. Practical notes

- Work in `open-enclose.github.io`; `pip install -e ".[dev]"`, then `pytest tests/`.
- `enclose.model` is numpy-only; `enclose.manufacturing` adds scipy (`brentq`).
- **`mu` gets accepted and then half-used.** This has now bitten three times: `tepvt_g`
  ignored it outright; `manufacturing` kept it in $\Lambda_\mu$ but dropped it from $A_\mu$
  (§3); and `mpl_a` defaulted to `mu=1` while `labor_share` and `excess_mpl` defaulted to
  `mu=0`, so the same defaulted call meant two different economies. All three are fixed and
  guarded. Assume the next one exists and test $\mu$ endpoints explicitly.
- **`model.weq` returns the commons *average* product for every $\mu$**, not the wage; the
  true wage is $A_\mu \cdot$ `weq`. Harmless in the two-sector model, where the level does
  not affect the allocation — which is exactly why it went unnoticed until manufacturing
  gave that level an allocative job. Anything new that reads `weq` as a wage needs the
  $A_\mu$ factor.
- `enclose.symbolic` derives every benchmark locus from its objective and checks the numeric
  layer against it. Nothing equivalent exists for the manufacturing case yet. The §3 sympy
  derivation was throwaway; folding it in is the natural guard against the next slip.
- The two drafts (§1) should be reconciled before any write-up. `enclosure_manuf.md` is
  canonical.
- `plotmpts` / `figures.labor_misallocation` still carries `TODO: not yet working for
  mu != 0`. If a welfare figure is needed for $\mu>0$, that must be fixed first.
