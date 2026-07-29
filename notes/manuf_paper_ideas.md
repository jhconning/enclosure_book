# Manufacturing paper — ideas and framing

**Created:** 2026-07-29. **Status:** working notes for a possible separate paper.

Derivations live in `docs/online_appendix.md` §6.4, eqs (35)–(43), implemented in
`open-enclose.github.io/enclose/manufacturing.py` with tests. This file carries the
*argument*: what is worth building, what is derivative, and what a paper would be.

History of the derivation, including three errors found and fixed:
[`MANUFACTURING_HANDOFF.md`](MANUFACTURING_HANDOFF.md).

---

## 1. The lead result

**$\Lambda_\mu < 1$ is simultaneously the condition for enclosure to release labor to
industry and the condition for the enclosure game to have strategic complementarities.**

Same inequality. Same threshold $\theta_H^\mu$. Both quantities flip sign there together —
$\partial l_m/\partial t_e$ and $dr/dt_e$ agree in sign at every $\theta$ tested, and both
pass through zero at $\theta_H$ exactly.

It is not a coincidence. Both are governed by whether enclosure raises or lowers labor
demand on the land. If enclosed land is less labor-hungry than the commons ($\Lambda_\mu<1$),
then enclosing releases labor *and* raises the return to further enclosure. One economic
force, two margins.

The consequence is the interesting part:

> **Everywhere enclosure feeds industrialization, the enclosure game has multiple
> equilibria. Where enclosure retards structural transformation, the equilibrium is unique.**

Regimes A and B — including the entire configuration the conventional account of enclosure
and industrialization presumes — lie inside the strategic-complements region. Regime C, where
enclosure draws labor back into agriculture, is the only one with a determinate equilibrium.

**So the enclosures that mattered for industrialization are precisely the ones whose timing
and occurrence were not pinned down by fundamentals.**

### Why this is the direction to build on

It is the only idea in these notes that the competing models cannot produce:

| | endogenous property rights | coordination failure | structural transformation |
|:---|:---:|:---:|:---:|
| Gollin–Parente–Rogerson | — | — | ✓ |
| Chen; Chen–Restuccia–Santaeulàlia-Llopis; Gottlieb–Grobovšek | — | — | ✓ |
| Demsetz (1967) and successors | ✓ | — | — |
| **this model** | ✓ | ✓ | ✓ |

Demsetz gets endogenous property rights but the response to rising land values is smooth and
determinate. The misallocation literature has the transformation but treats property rights
as an exogenous treatment. GPR has neither.

### What it explains

**Enclosure came in bursts** — Tudor, then parliamentary 1760–1830 — not smoothly with rising
grain prices. A Demsetz mechanism predicts smooth adjustment to rising land values. A tipping
game predicts bursts, with timing that depends on history rather than only on fundamentals.

Combined with the price channel (§6.3 below) this gives a mechanism: gradual growth in
manufacturing productivity raises food prices, raises land rents, and at some point tips a
coordination game that then moves fast. **Gradual technology, discontinuous institutions.**

### The paper this implies

*Coordination failure and the timing of structural transformation.* Set $\theta=1$ throughout
to remove the technology confound. Closed economy so the relative price does the work. The
claim: two economies with identical technology paths industrialize at different dates because
the enclosure game tipped at different times, and the tipping is history-dependent.

GPR explain industrialization dates by agricultural TFP. This says part of the variance is
coordination — and, unlike a residual, says which part and what it should correlate with.

The reversal result (§3.3) becomes the **empirical arm**: within that framework the
labor-release effect should be weakest where the productivity gain is largest. Clean,
falsifiable, inverts the received view, testable on enclosure-award data. A strong section,
not a paper.

---

## 2. Honest ranking of everything else

Assembled over a long working session, and most of it is derivative. Recorded here so the
same enthusiasm is not spent twice.

| Idea | Prior art | Verdict |
|:---|:---|:---|
| Coordination ⟺ labor release (§1) | none found | **Build on this** |
| Labor release weakest where productivity gain largest (§3.3) | sign reversals are a genre (Matsuyama 1992), but not this one | **Strong — the empirical arm** |
| Endogenous selection into titling biases the misallocation literature (§6.2) | — | **Good, but a comment not a paper** |
| Commons as microfoundation for Lewis's institutional wage (§5) | Sen (1966); the surplus-labor debate; Gottlieb–Grobovšek | Exposition, not contribution — *demoted* |
| Governance dominates enclosure at $\theta=1$ (§4.4) | de Meza–Gould (1992), cited 10× in the paper already; Ostrom | Incremental |
| Commodity boom triggers enclosure (§6.3) | **Demsetz (1967)** — this is his canonical mechanism | Derivative; our increment is the multiplicity |
| Distribution → home market → divergent paths (§6.4) | Murphy–Shleifer–Vishny (1989); Galor–Moav–Vollrath | Derivative, and expensive to model |
| Perverse $\mu$–$\tau$ interaction | Lipsey–Lancaster; §5.3 already asserts it | Quantification of a claim already made |
| $\tau^*=1$ at $(\theta_H^\mu)^\alpha$ | — | Cute Cobb–Douglas knife-edge; report, don't build |

Attributions are from memory and **not checked against sources**. The Gottlieb–Grobovšek
reading matters most, since the "we microfound them" claim in §6.2 depends on their friction
being what I think it is. PDFs are in `Y:\B\zot_pdfs\`.

---

## 3. The formal core

Full derivations in `docs/online_appendix.md` §6.4. Notation: $\alpha,\beta$ = labor shares,
$\theta$ = relative TFP of enclosed land, $t_e$ = enclosed share, $l_m$ = manufacturing labor
share, $\mu$ = governance, $\tau$ = compensation, $c$ = enclosure cost,
$\Lambda_\mu=\left(\frac{\alpha\theta}{1-\mu(1-\alpha)}\right)^{1/(1-\alpha)}$,
$\Lambda_o=\theta^{1/(1-\alpha)}$, $\theta_H^\mu = \frac{1-\mu(1-\alpha)}{\alpha}$.

### 3.1 The governance wedge, eq. (37)

$$A_\mu = 1-\mu(1-\alpha), \qquad A_0=1,\quad A_1=\alpha$$

The share of the commons average product labor takes home — its marginal product plus the
fraction $(1-\mu)$ of possession rents it retains. Derived from the Euler decomposition (8)
and eq. (22); nothing new assumed. $\Lambda_\mu$ carries $\mu$ into the *slope* of the labor
allocation, $A_\mu$ into the *level* of what labor earns.

### 3.2 The manufacturing margin, eqs. (38)–(39)

$$\frac{l_m^{1-\beta}}{(1-l_m)^{1-\alpha}} = \frac{C_m}{C_a},\qquad
C_m = p\beta\bar k^{1-\beta},\quad
C_a = A_\mu\bar t^{1-\alpha}(1+(\Lambda_\mu-1)t_e)^{1-\alpha}$$

Unique equilibrium. Transcendental for $\beta\neq\alpha$; at $\beta=\alpha$,
$l_m = R/(1+R)$ with $R=(C_m/C_a)^{1/(1-\alpha)}$. At $t_e=1$ there is no commons, so
$C_a = \alpha\theta\bar t^{1-\alpha}$ for every $\mu$ — full enclosure implements the
planner's inter-sectoral allocation for any $\theta$, *conditional on $t_e$*.

### 3.3 The reversal at $\theta_H^\mu$

$$\operatorname{sign}\left(\frac{\partial l_m}{\partial t_e}\right)=\operatorname{sign}(1-\Lambda_\mu)$$

Below $\theta_H^\mu$ enclosure accelerates structural transformation; above it, retards it;
at it, moves no labor. Exact knife-edge. **This is the same condition as strategic
complementarity — see §1.**

### 3.4 The planner's enclosure margin, eq. (40)

$$\frac{dY}{dt_e}=(1-\alpha)\bar t^{1-\alpha}(\Lambda_o-1)\left(\frac{1-l_m(t_e)}{1+(\Lambda_o-1)t_e}\right)^{\alpha}$$

The benchmark's $z'(t_e)$ with the agricultural labor share replacing the whole labor force.
Sign is that of $(\theta-1)$ — note $\Lambda_o$, **not** $\Lambda_\mu$. This margin turns at
$\theta=1$, the labor reversal at $\theta_H^\mu$: *is enclosure worth doing* versus *which way
does it push labor*. Hence $t_e^o=0$ for every $c>0$ whenever $\theta\le1$.

### 3.5 Three regimes, eq. (41)

$$\theta_H^\mu - 1 = \frac{(1-\alpha)(1-\mu)}{\alpha}\ \geq 0,\quad =0 \text{ iff } \mu=1$$

| Regime | $\theta$ | Efficient? | Labor | Enclosure game |
|:---|:---|:---|:---|:---|
| A | $<1$ | No, at any $c>0$ | Released | **Complements — multiple equilibria** |
| B | $1$ to $\theta_H^\mu$ | Yes, if $c$ small | Released | **Complements — multiple equilibria** |
| C | $>\theta_H^\mu$ | Yes, if $c$ small | Drawn back into agriculture | Substitutes — unique |

Regime B is the conventional account's configuration; its width is proportional to $(1-\mu)$,
so it exists only to the extent the commons is badly governed. The last column is §1.

### 3.6 Compensation, eqs. (42)–(43)

$$r^e_\mu-\tau r^c_\mu = (1-\alpha)A\bar l^\alpha\left(\frac{1-l_m}{1+(\Lambda_\mu-1)t_e}\right)^\alpha\big[\theta\Lambda_\mu^\alpha-\tau\big],\qquad
\tau^*=\theta\Lambda_\mu^\alpha$$

Manufacturing enters only through $(1-l_m)^\alpha$; $\tau$ only the bracket. $\tau$ moves
neither threshold — **$\mu$ changes what enclosure would do; $\tau$ changes whether it
happens.** $\tau^*\lessgtr1 \iff \theta\lessgtr(\theta_H^\mu)^\alpha$.

### 3.7 Verification status

| Result | Checked how |
|:---|:---|
| (37) wedge / planner FOCs | sympy; Nelder–Mead on the objective; equal-return system from primitives |
| (39) uniqueness, closed form | parameter sweep; $\beta=\alpha$ oracle to 12 s.f. |
| (39) reversal sign | numerical derivative across $\alpha$, $\mu$, both sides of $\theta_H$ |
| §1 coordination ⟺ release | signs of $\partial l_m/\partial t_e$ and $dr/dt_e$ agree at all $\theta$ tested |
| (40) envelope | central difference of the value function, 12 $(\theta,t_e)$ points |
| (41) band width | exact, 12 $\alpha\times\mu$ combinations |
| (42) factorization | 27 cases against rentals from marginal products |
| (43) $(\theta_H^\mu)^\alpha$ | exact, 12 $\alpha\times\mu$ combinations |

184 tests pass. **Not checked:** the decentralized $t_e$ under strategic complementarity needs
the global-games refinement (15); the $\tau$ table in §4.5 uses the marginal condition directly.

---

## 4. Interpretation

### 4.1 A dividend you can only collect in person

Open access is the fishery problem run through people. A commoner is not paid a wage — they
keep labor's worth *plus* a slice of the land's worth, and collect the slice only by standing
on the land. Leaving forfeits not the wage but the claim. Formally $A_0=1$: labor captures the
entire average product.

**The problem is not that commoners receive the rent. It is that they can only receive it in
person.** That sentence carries most of the argument.

### 4.2 Enclosure releases labor by cancelling the dividend

At $\theta=1$ — no productivity gain by construction — manufacturing's share goes from 20% to
68% and output rises 13%. Industry gains workers because agriculture stops overpaying them.
Measured output per worker rises sharply and looks like a productivity revolution; it is
reallocation.

### 4.3 Wages fall while output rises

Income per worker falls 31% while output rises 13%. Before: labor's worth plus the dividend.
After: labor's worth alone. Both sides of the standard-of-living debate are right about
different objects; the dividend was a claim on rent and enclosure transferred it.

### 4.4 Regimes and historical accounts

*(Migrated from the online appendix, where interpretation did not belong.)*

**Regime A with weak compensation is the expropriation account** — primitive accumulation in
the Marxian tradition, and the redistributive readings of Thompson and Allen. The model makes
the combination precise: enclosure that *reduces* agricultural output, privately profitable
only because the displaced are not compensated ($\tau<\tau^*$), and simultaneously driving
labor into industry. Expropriation and industrialization are not two things that coincided —
they are the same movement of people, and what permits it is $\tau$, not $\theta$.

**Regime B is the optimistic account** (Chambers and after), split at $(\theta_H^\mu)^\alpha$
into B1 where a compensation requirement blocks a socially valuable transition and B2 where it
is a pure transfer. Alike in enclosure rates, opposite responses to compensation rules.

**Regime C has no standard narrative**, which is informative. Enclosure that draws labor *out*
of manufacturing is not the English story but reads naturally as commercial-estate and
plantation expansion — belongs with the frontier material of §6.3 of the appendix, not the
industrialization debate.

$\tau$'s historical referent: parliamentary enclosure with commissioners and allotments is
high-$\tau$; enclosure by agreement or unity of possession is low-$\tau$.

**Stinting was the alternative, and it existed.** English commons were routinely stinted —
each commoner limited to a fixed number of beasts, enforced through the manor court. That is
$\mu$, and it reaches the identical allocation without survey, fence or litigation. Ostrom's
argument as arithmetic. Modern reading: titling is worth its cost when it makes land more
productive, not when it merely gets people to move.

### 4.5 The perverse interaction

At $\theta=1$, $c=0.05$, output net of cost (equilibrium $t_e$ in parentheses):

| | $\tau=0$ | $\tau=0.5$ | $\tau=1$ |
|:---|:---|:---|:---|
| $\mu=0$ | 1.347 (1.00) | 1.236 (0.00) | 1.236 (0.00) |
| $\mu=0.5$ | 1.347 (1.00) | 1.347 (1.00) | 1.335 (0.00) |
| $\mu=1$ | 1.347 (1.00) | 1.347 (1.00) | **1.397** (0.00) |

$\partial Y/\partial\tau$ flips sign with $\mu$. Compensating without regulating blocks the
only useful thing enclosure was doing; regulating without compensating leaves enclosure
happening as deadweight loss of exactly $c$.

---

## 5. The Lewis framing — exposition, not contribution

**Demoted.** Sen (1966) has the family farm allocating labor to average product, and the
surplus-labor debate is built on the APL/MPL wedge; Gottlieb–Grobovšek have the land-claim
version quantitatively. Our increment is that the wedge is tied to $\alpha$ rather than free.
Real but small. Use this section to make the paper legible to a development audience — not as
the claim to novelty.

What is worth keeping from it:

**It survives Schultz's critique.** The strong Lewis form has $MPL=0$ in agriculture, which
the 1918–19 influenza evidence is taken to have refuted. Ours never claims it:
$MPL_c=\alpha\cdot APL_c>0$ throughout, and surplus labor is the *allocation gap*, not a stock
of zero-product workers. Remove workers and output falls, exactly as observed, with the
misallocation intact.

**Three routes to the same turning point.** Take the baseline to $l_m=0.68$ three ways
($\alpha=0.4$, $\beta=0.7$, $\theta=1$; "workers' total" includes retained commons rent):

| Route | $l_m$ | wage | workers' total | output |
|:---|---:|---:|---:|---:|
| baseline: open-access commons | 0.197 | 1.140 | 1.140 | 1.236 |
| **(i)** full enclosure | 0.676 | 0.787 | 0.787 (−31%) | 1.397 (+13%) |
| **(ii)** regulated commons | 0.676 | 0.787 | 1.169 (**+2.5%**) | 1.397 (+13%) |
| **(iii)** Lewis growth ($p$: 1→2.5) | 0.676 | 1.968 | 1.968 (+73%) | 2.538 (+105%) |

(i) and (ii) are identical in allocation, wage and output; they differ only in whether the
land rent — 60% of agricultural output — stays with the commoners. (iii) is the only route
where the wage rises.

**Hence: the agricultural labor share cannot identify the mechanism; the wage can.** A
transition where the farm workforce collapses *and* real wages fall is not a Lewis transition,
whatever the sectoral data look like. This is the one part of the Lewis material that is ours,
and it is a usable diagnostic.

**Portable claims.** If the distortion is that the claim must be collected in person, the fix
is to make it portable rather than to abolish it. PROCEDE certification of Mexican ejidos made
rights secure without requiring presence, and the migration response is documented (de Janvry
et al., already cited in the paper) — close to a direct test.

---

## 6. Relation to the dynamic literature

### 6.1 Gollin–Parente–Rogerson

Their agriculture uses **only labor**; they note explicitly that adding land "would have no
impact on our results." That is true within their model precisely because there is no
property-rights wedge on land — so our entire mechanism lives in the space they assume away,
and their justification for assuming it away presupposes what we deny.

**Two theories of why labor stays on the land.** GPR: labor stays because it is *needed* —
$N_a=\bar a/A_a$, efficient given the subsistence constraint, no wedge anywhere. Ours: labor
stays because it is *paid to*.

They are separately identifiable:

> Is agricultural output per capita comfortably above subsistence while the agricultural
> employment share stays high?

If yes, the food constraint has slackened and labor still has not moved. Much of sub-Saharan
Africa looks like this. No structural estimation needed.

Second discriminator: in GPR agricultural output can never fall below $\bar a$. In ours,
enclosure-driven transformation *reduces* food output (0.916 → 0.637 at $\theta=1$). Episodes
where the farm workforce collapsed and food output fell are outside GPR by construction.

### 6.2 The misallocation papers

**Gottlieb–Grobovšek** is closest: communal tenure where rights lapse on migration is our
dividend-collected-in-person, imposed as a friction. We would microfound it — the wedge is not
a free parameter but exactly $(1-\mu)(1-\alpha)APL$, which yields a restriction their
calibration cannot make: **the migration wedge should scale with land's factor share.**
*(Verify their setup before relying on this.)*

**Chen; Chen–Restuccia–Santaeulàlia-Llopis** treat titling as exogenous and ask "what if
titled?" Three problems with that counterfactual: titling costs $c$ and theirs is typically
costless; there are *two* ways to remove the distortion, so the right comparison is titling vs
governance, not titling vs status quo; and removal is not Pareto-improving, since aggregate
TFP gains conceal a transfer of $(1-\alpha)$ of agricultural output.

**And the sign can flip.** Their frameworks find titling releases labor; $\theta_H$ says that
holds only below the threshold. Worth checking whether any of them found a perverse labor
effect and treated it as a puzzle.

**Endogenous selection into titling.** All treat property rights as policy. If reform happens
where rents are largest — and, per §1, where coordination succeeded — then selection into
reform is endogenous and their estimates are plausibly biased upward. A methodological
critique with teeth, but a comment or a section, not a paper.

### 6.3 The price channel — Demsetz with multiplicity

In partial equilibrium enclosure rents scale with $(1-l_m)^\alpha$, so industrialization
*discourages* enclosure. Close the economy and add a food constraint and it inverts: labor
leaving agriculture raises $p_a$, raises land rents, encourages enclosure. **The sign of the
feedback depends on the closure.**

Two testable consequences: repeal of the Corn Laws should have cut the return to enclosure by
severing the price channel; and commodity price booms should trigger enclosure — the 2007–08
food price spike and the subsequent surge in large-scale land acquisition.

**But this is Demsetz (1967).** Rising resource values induce private property is his canonical
mechanism. Our increment is that the response is discontinuous and history-dependent rather
than smooth — which only matters because of §1. State it that way or not at all.

Open modelling question: rising $p_a$ raises rents (more enclosure) but also raises the
agricultural return to labor (pulls labor back). Whether that is explosive, oscillatory or
self-correcting is unknown.

### 6.4 Distribution and the home market

Two economies reaching the same allocation, one by enclosing and one by stinting, hold the
$(1-\alpha)$ rent differently. With non-homothetic preferences that changes demand
composition, hence $p$, hence the enclosure incentive. Distribution drives structural
transformation in a way a representative agent cannot produce.

This is Murphy–Shleifer–Vishny (1989) with a property-rights microfoundation, and it sits in a
large land-inequality-and-development literature. Real but incremental, and expensive to model.
**Park it.**

---

## 7. What to build

**Minimal dynamic model.** GPR's labor allocation is static within each period, so bolt our
structure on as a sequence of static equilibria with capital accumulating GPR-style:
Stone-Geary $\bar a$; agriculture with land and the commons/enclosed split; manufacturing with
capital; closed economy so $p$ clears the food market; exogenous $A_a(t)$, $A_m(t)$; and $t_e$
from the enclosure game each period.

**Simplifications to take.**
- Set $\theta=1$ throughout. All the sharp results live there and it removes the technology
  confound. The paper becomes *structural transformation without productivity growth*.
- Keep the global-games refinement — it is the point, per §1, not a complication to drop.
- Sequence of statics, not full dynamic optimization.
- Leave $\tau$ out of the first pass; it is a transfer and the coordination story does not
  need it.

**The figure the paper turns on:** two economies, identical $A_a(t)$ and $A_m(t)$, different
industrialization dates, because the enclosure game tipped at different times.

---

## 8. Open questions

**Formal.** Decentralized $t_e$ with a manufacturing outside option — closes the loop and is
what turns this from an extension into a paper. Global-games refinement applied to §3.6.
Endogenous $p$. Fold the manufacturing derivations into `enclose.symbolic` (three algebra
errors in this material argue for it).

**Empirical.** The yield-gain vs out-migration horse race on enclosure awards. Parliamentary
vs by-agreement enclosure as high- vs low-$\tau$. The wage diagnostic (§5) applied to episodes
usually classed as Lewis transitions. Whether enclosure actually came in bursts, and whether
the bursts line up with price movements or not — §1 predicts *not* cleanly, which is the test.

**Reading owed.** Gottlieb–Grobovšek, Chen (2017), Chen–Restuccia–Santaeulàlia-Llopis, all in
`Y:\B\zot_pdfs\`. Also Sen (1966), Demsetz (1967), Matsuyama (1992) to confirm the §2
attributions. None of §2's prior-art claims have been checked against sources.

---

## 9. Provenance

Numbers in §4 and §5 are computed from `enclose/manufacturing.py`. Three errors were found and
corrected in this material — a missing $A_\mu$ that inverted the welfare comparison, an
over-reach from the labor margin to the enclosure margin, and a backwards sign statement — all
documented in [`MANUFACTURING_HANDOFF.md`](MANUFACTURING_HANDOFF.md) §3–§4. The pattern in all
three: a claim true in the $\mu=0$ or conditional-on-$t_e$ case, restated without its qualifier.

The §1 result was found late, after several rounds spent on the Lewis framing that §2 now
demotes. It is a two-line analytical observation about machinery the paper already had.
