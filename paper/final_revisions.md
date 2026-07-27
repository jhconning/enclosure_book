# Final Revisions Guide — RESTUD MS-36173 (Conditional Acceptance)

**Paper:** *A Model of Enclosures: Coordination, Conflict, and Efficiency in the Transformation of Land Property Rights* (Baker & Conning)

**Status:** Conditionally accepted at *The Review of Economic Studies* (editor: Bård Harstad).
This document organizes the final revision into phases. It is a guide for editing `main.tex` — no edits have been made yet. Line numbers refer to the current `paper/main.tex` (740 lines, matching the compiled `Baker_Conning_EnclosuresRESTUD.pdf` of July 24, 2026).

**Editor's requirements (from `referee_reports/cond_accept/editor_email.md`):**

| Item | Requirement | Source |
|------|-------------|--------|
| (i) | Fix long sentence in Abstract; **delete final Abstract sentence** | R1 pt 2 + editor |
| (ii) | R1's points 3 and 4 ("very sensible") | R1 pts 3, 4 |
| (iii) | Graphically show how parameter changes move the equilibrium; relate to over/under-enclosure predictions | R2 (+ helps R5 pt 1) |
| (iv) | **Remove Section 6.4** (Structural transformation) | R2 + editor |
| (v) | Define "enclosure decisions are strategic complements" plainly | R5 pt 5 |

Anything done *beyond* (i)–(v) must be listed in the cover letter to the editor. No referee reports needed this round.

---

## Phase 0 — Mechanical fixes (do first; uncontroversial)

All verified present in both `main.tex` and the compiled PDF.

| # | Location | Current | Fix |
|---|----------|---------|-----|
| 0.1 | line 624 (§6.3, end of Wakefield/Domar paragraph) | Stray word `Faust` alone after `\citep{binswanger1993, solberg1969, legrand1984}.` (visible in PDF p. 35) | Delete `Faust` |
| 0.2 | line 721 (Conclusion, 1st para) | `tip into dissipative races, or or fall short` | Delete duplicate `or` |
| 0.3 | line 341 (§3.4, 1st sentence) | `in the low-TFP region multiple equilibria region` | → `in the low-TFP multiple-equilibria region` |
| 0.4 | line 139 (footnote 4) | `when we affect a decomposition` | → `when we effect a decomposition` (or reword: `when we decompose the various costs and benefits`) |
| 0.5 | line 342 (footnote 11) | `standard conditions \citet[Sections~2.1--2.2]{morris2003}` | → `\citep[Sections~2.1--2.2]{morris2003}` (parenthetical) |
| 0.6 | line 292 (Prop. 2, partial enclosure bullet) | `$r(t_e^{o})=c$` | → `$r(t_e^{*})=c$` for consistency with `$t_e^* \in (0,1)$` in same bullet |
| 0.7 | line 404 (Prop. 4 statement) | `labor reaction rule $l_e^o(t_e)$` | → `$l_e^0(t_e)$` (zero superscript, matching eq. (10)/`\ref{optle0}`) |
| 0.8 | lines 380, 449 | `on figure \ref{fig_compare}`, `from figure \ref{figure_private}` | → `Figure` (capitalize; check globally with grep for `figure \\ref`) |
| 0.9 | `references.bib` Marx entry | Renders as `Marx [1867] (Marx, Karl). 1992.` and **sorts first, out of alphabetical order** (PDF p. 40) | Fix the biblatex-chicago entry: use `author = {Marx, Karl}`, `year = {1992}`, `origdate = {1867}`, and remove whatever `sortname`/`shorthand`/`options` field is forcing the bracketed prefix and mis-sorting. Target rendering: "Marx, Karl. (1867) 1992. *Capital…*" alphabetized under M |
| 0.10 | Title footnote (line 48) | PDF p. 1 appears to render `…to replicate all figures is is at` | Verify the submitted source; if "is is" is present, delete one "is" |
| 0.11 | line 721 | `We identify the precise conditions` — same sentence as 0.2; while editing, re-read whole sentence aloud | Combined fix with 0.2 |

**Also worth checking while in Phase 0** (cosmetic, zero risk):
- Line 549: "In the left-hand panels of the figure, constrained-optimal decisions are characterized by the blue dashed lines, which may be relevant in this parameter range." — vague; say what the dashed lines are, e.g. "The blue dashed lines in panels (a) and (c) mark the constrained (second-best) planner's thresholds from Section 4.1." (This dovetails with R5 pt 3, Phase 2.3.)
- Figure file name `new_comp_fig4x4.png` and label `figure4x4` are internal only — fine to leave.

---

## Phase 1 — Editor-required changes (i)–(v)

### 1.1 (i) Abstract: shorten the long sentence; delete the last sentence

**Problem sentence** (lines 57): *"Depending on the balance of these fundamentals, enclosure decisions may be strategic complements, generating abrupt tipping points and socially destructive property races, or strategic substitutes, leading to smooth transitions but insufficient enclosure when private returns fall short of social gains."* R1 finds it long and unclear; the editor agrees.

**Suggested replacement** (splits into two sentences and states the mechanism in plain words):

> *"When productivity gains from enclosure are small, each enclosure displaces labor onto the remaining commons, raising the return to further enclosure: decisions become strategic complements, generating tipping points and socially destructive property races. When potential gains are large, enclosure instead pulls labor out of the commons and raises wages, so transitions are smooth but may stop short of the social optimum."*

(Adjust to taste — the key is one clause per idea, and naming the displacement/absorption mechanism rather than the game-theory jargon alone. This also pre-answers R5's point 5 in the abstract itself.)

**Delete the final sentence** (editor's explicit request): *"Our analysis provides a unified framework for evaluating mechanisms emphasized in Neoclassical, Neo-institutional, and Marxian interpretations of historical enclosure processes and contemporary land formalization policies."*

Note: if deleted verbatim, consider whether the preceding sentence ("While policies to strengthen customary governance…can worsen welfare.") now ends the abstract adequately — it does, on the paper's second-best punchline.

### 1.2 (ii-a) R1 pt 3: "first-best" vs "second-best" shading (p. 21 / line 449)

**Current text** (line 449): *"Figure 5 overlays the constrained planner's decision regions on the decentralized economy's enclosure regions from figure 4, with first-best regions shown in lighter shading."*

**Action:** Verify against `Figures/comparison.png` and the generating code (`notebooks/enclose.py` / plotting notebook) what the lighter shading actually depicts.
- If the light shading depicts the *first-best* partial-enclosure band (the `\bar l_0^1`–`\bar l_1^1` band carried over from Fig. 1), the text is technically right but confusing, since the whole paragraph is about the constrained (second-best) planner. In that case rewrite for clarity, e.g.: *"…with the first-best regions of Figure 2 retained in lighter shading for comparison."*
- If the shading actually shows second-best regions, correct to "second-best" as R1 suspects.

Either way, R1's confusion signals the caption of Figure 5 should also name each region explicitly (ties into R5 pt 3 / Phase 2.3).

### 1.3 (ii-b) R1 pt 4: show how τ enters the model in §5.2, not §5.3

**Problem:** §5.1 (regulated commons) introduces μ with an explicit equilibrium condition (eq. 22). §5.2 (Power and Compensation) describes τ only verbally; the reader first sees τ in a formula in §5.3 (eq. 23, `tau_enclose`, lines 508–511). R1 read back and forth looking for it.

**Suggested fix (minimal, structure-preserving):** move eq. (23) and its one-sentence setup from the start of §5.3 up into §5.2, right after the paragraph introducing τ (line 502–504). Concretely, insert at the end of §5.2:

> *"With compensation requirements, the private encloser's decision rule changes. For each enclosed unit, the encloser must pay $\tau \cdot r_c$ to existing users, where $r_c = F_T^c A \bar f$ is the land rent those users captured through possession. Enclosure is privately profitable when*
> $$\theta F_T^e A \bar f - \tau \cdot F_T^c A \bar f - c \geq 0. \tag{23}$$
> *When $\tau = 1$, enclosers fully internalize displaced rents; when $\tau = 0$, enclosure is a pure 'raid.'"*

Then §5.3 ("The Extended Wedge") opens directly with the recap of the decomposition and the combined-wedge equation (24), referring back to (23). This makes §5.1/§5.2 symmetric (each parameter gets its defining equation) exactly as R1 asks. Renumber/check `\ref{tau_enclose}` references (used at lines 512, 520, 606).

### 1.4 (iii) New figure: parameter-change trajectories (R2's request; helps R5 pt 1)

**R2's ask (endorsed by editor):** *"graphically show how particular parameter changes (e.g. in τ or c/A or l̄) change the equilibrium from one point to the other and how these relate to the main theoretical predictions of over- or under-enclosure,"* possibly labeling points "Weitzman–Samuelson," "Marx," "De Janvry," etc.

**Key geometric fact that organizes the whole figure:** every boundary locus in the paper has the form $\ln\bar l = \frac{1}{\alpha}\ln(c/A) + g(\theta)$ — eqs. (6), (7), (14), (15), (17) all scale as $(c/A)^{1/\alpha}$. A fall in $c/A$ therefore shifts *every* locus down by the same vertical distance, which is geometrically identical to the economy's point moving *up* against fixed loci. So shocks to $\bar l$, $c$, and $A$ can all be drawn as **vertical arrows on one fixed canvas**; only the institutional parameters ($\tau$, $\mu$) genuinely require showing a locus move. This splits the figure naturally into two panels. (State the equivalence in the figure note — it is itself a useful result for readers.)

**Suggested implementation — one two-panel figure in Section 6**, built from the existing Figure 5 code (all loci in `notebooks/enclose.py`; annotations via matplotlib `annotate()`; new output `Figures/trajectories.png`). Canvas: $(\theta, \ln\bar l)$, $\alpha = 2/3$ so $\theta_H = 1.5$, $c/A = 1$, dotted verticals at $\theta = 1$ and $\theta_H$, decentralized loci in red ($\bar l_{gg}^d$ dashed on low-TFP side; $\bar l_0^d$, $\bar l_1^d$ on high-TFP side), second-best loci in blue, over/under-enclosure hatching as in Figure 5.

**Panel (a) — movements in fundamentals (loci fixed at benchmark μ = τ = 0):**

| Element | Placement | Response shown | Narrative |
|---|---|---|---|
| Point **"Weitzman–Samuelson"** | On the θ = 1 line, below $\bar l_{gg}^d$ | Commons persists; any enclosure would be pure redistribution | Weitzman (1974), Samuelson (1974) |
| Arrow **"Boserup"** | Vertical ↑ at θ ≈ 2, crossing $\bar l_0^d$ | **Continuous**: partial enclosure begins at crossing, $t_e^*$ rises smoothly | Hayami–Ruttan; Holden et al. |
| Arrow **"Barbed wire / cheap titling"** | Vertical ↑ of the **same length** at θ ≈ 1.2, crossing $\bar l_{gg}^d$; label crossing "tipping point" | **Discontinuous**: $t_e$ jumps 0 → 1 → over-enclosure | Hornbeck (2010); titling programs |

The two same-length arrows with opposite-character responses are the panel's punchline — exactly R2's "sudden switch between corners" point (smooth in the substitutes region, tipping in the complements region).

**Panel (b) — movements in institutions (economy's point fixed):**

| Element | Placement | Response shown | Narrative |
|---|---|---|---|
| $\bar l_{gg}^d$ drawn **twice**: solid (τ = 0) and shifted up (τ = 1) | Low-TFP side | Compensation raises the density needed before raiding pays | Anderson–McChesney "raid vs trade" |
| Point **"Marx / Brenner"** between the two gg loci at θ ≈ 1.1 | Between τ = 1 and τ = 0 loci | Power shift (τ↓) sweeps the locus past the point → cascade **with no change in fundamentals**; labor immiserated since θ < θ_H | Brenner; post-1865 U.S. frontier |
| Arrow on the $\theta_H^\mu$ line, pushing left from 1.5 (μ = 0) toward 1 (μ = 1) | Vertical dotted line | Stronger customary governance shrinks the race-prone (complements) region | Ostrom; eq. (26) |
| *(Optional)* Point **"De Janvry"** in high-θ band between $\bar l_0^s$ and $\bar l_0^d$ | Under-enclosure region | Beneficial transition blocked; functional dualism | de Janvry (1981) |

**Associated comparative-statics table** (place adjacent to the figure; content is a tabulation of §3.5's existing prose + Figure 6's panel logic, so nearly free to write). Five rows × five columns — *parameter change → geometry in figure → equilibrium response → efficiency verdict → narrative/citation*:

| Change | In the figure | Equilibrium response | Efficiency | Narrative |
|---|---|---|---|---|
| $\bar l \uparrow$ | Vertical arrow up, panel (a) | Smooth $t_e\uparrow$ if $\theta>\theta_H$; jump at $\bar l_{gg}^d$ if $\theta<\theta_H$ | Efficient if θ high; race if low | Boserup; Hayami–Ruttan |
| $c/A \downarrow$ | Same vertical arrow (loci scale as $(c/A)^{1/\alpha}$) | Same as $\bar l\uparrow$ | Titling subsidies can tip stable commons into a race | Hornbeck; de Soto-style programs |
| $\theta \uparrow$ | Horizontal arrow right; may cross $\theta_H^\mu$ | Regime switch complements→substitutes; labor switches loser→gainer at $\theta_H^\mu$ | Under-enclosure becomes the risk | Allen vs. Heldring et al. |
| $\tau \downarrow$ | Decentralized loci sweep down, panel (b); planner loci fixed | Enclosure where none occurred before | Over-enclosure region expands; raids even at θ ≤ 1 | Brenner; Anderson–McChesney |
| $\mu \uparrow$ | $\theta_H^\mu$ moves left toward 1 | Less misallocation; labor-gains threshold falls | Under-enclosure shrinks; over-enclosure expands if τ = 0 (second-best warning) | Ostrom; ejido reforms (de Janvry et al. 2015) |

Recommended framing paragraph opening §6: *"Figure X positions several canonical narratives from the literature as parameter configurations or comparative-static paths in the model's parameter space; Table Y summarizes the direction and efficiency verdict of each movement. Movements that cross the decentralized loci but not the planner's loci (or vice versa) identify the over- and under-enclosure predictions of Section 4."* R2 explicitly accepts these are "speculative hypotheses … amenable to falsification" — a candid sentence to that effect is appropriate and cheap.

Design notes:
- Division of labor: the **figure** shows trajectories and the smooth-vs-sudden contrast (R2's core request); the **table** states signs, geometry, and the over/under-enclosure verdict per parameter (R5 pts 1–2; the editor expects item iii to "also help you address R5's first point").
- Keep each panel to 3–4 labeled elements — orientation, not completeness.
- Reuse the exact loci from Figure 5; no new derivations.
- §6.4's removal (item 1.5) frees the space; net page count roughly unchanged.
- If the table above is adopted, it can *absorb* the "effect of an increase" role, letting the Phase 2.2 symbol table stay purely definitional (avoid duplicating content between the two tables).
- Cross-reference the new figure from the introduction (one sentence) to serve R5's pt 1.

### 1.5 (iv) Remove Section 6.4 (Structural transformation and manufacturing)

**Editor:** "I agree, because it did not add as much as the other parts of the paper."

**Recommendation: move, don't destroy.** Transfer §6.4 (lines 678–717) to the **online appendix** (https://open-enclose.github.io/), and replace it in the paper with nothing (renumber) — at most a single sentence + footnote at the end of §6.3 or in the §6 overview paragraph:

> *"An online appendix extension adds a manufacturing sector and examines how enclosure interacts with structural transformation; see also the discussion of selection and occupational choice there."*

**Knock-on edits checklist:**
1. Delete/redirect the §6 roadmap sentence (line 573): *"Section \ref{manuf_sec} sketches implications for structural transformation and the macro-misallocation literature."*
2. Introduction roadmap (line 91) — doesn't name 6.4 individually ("Section 6 applies the framework…"), so no change needed; verify.
3. Search for `manuf_sec` cross-references anywhere else (`grep -n "manuf_sec" main.tex`).
4. The Allen/Heldring historiography paragraph that currently *opens* §6.4 (lines 680–682) is valuable and partially duplicated in §6.2 (lines 612). Check whether anything from it should be salvaged into §6.2 rather than lost — recommend salvaging the Lewis-surplus-labor sentence into §6.2's English-enclosures paragraph if it isn't redundant.
5. Bibliography: biber will automatically drop now-uncited items (lewis1954, cohen1975, crafts2004, chen2017a possibly) — no manual action, but rebuild and check.
6. **Resolves the R1 pt 1 conflict** (see Phase 2.1): the discussions promised to R1 "in Section 6.4" go to the online appendix alongside the moved section, and this is explained in the cover letter.

### 1.6 (v) Define "strategic complements/substitutes" plainly (R5 pt 5)

R5: *"What does it mean to say 'enclosure decisions are strategic complements'? How does one decision complement or substitute for another?"* The editor: "this should be simple for you to define."

**Two insertions:**

(a) **Introduction, first use (line 81).** Insert a defining clause at first mention, e.g.:

> *"…enclosure decisions are* strategic complements *— each act of enclosure raises the private return to enclosure for others, so decisions reinforce one another — when productivity gains to enclosure are modest or nonexistent."*

and symmetrically at line 83 for substitutes: *"…*strategic substitutes*: each enclosure lowers the return to further enclosure, so individual decisions partially offset one another."*

(b) **Section 3.3, at Proposition 1 (line 276).** Add one plain-language sentence immediately before or after the proposition:

> *"Formally, enclosure decisions are strategic complements (substitutes) when the equilibrium return to enclosing, $r(t_e)$, is increasing (decreasing) in the aggregate enclosure rate $t_e$: one player's enclosure raises (lowers) every other player's incentive to enclose."*

(c) **R5's sub-nit (demand vs. supply):** In the paragraph following Prop. 2/3 (line 312, "The contrast between Propositions 2 and 3 reflects fundamentally different labor market responses…"), make explicit which side of the labor market moves: low-θ enclosure *releases labor* (a labor-**supply** shift onto the commons/market that depresses wages); high-θ enclosure *raises labor demand* (a labor-**demand** shift that bids wages up). Two clause-level edits suffice — the sentences already carry the substance.

---

## Phase 2 — "Consider" items (optional; each done item must be flagged in the cover letter)

The editor: *"I do not request that you do the other changes suggested in the attached reports, but I request that you consider them."* Recommendations below.

### 2.1 R1 pt 1 — the promised-but-missing §6.4 discussions ⭐ RECOMMEND

**Background:** In the last round, `ResponseR1.tex` told R1 that two discussions had been "added to Section 6.4": (a) the constant-wage / unlimited-labor-absorption manufacturing limit (R1's old pt 3), and (b) the selection / span-of-control channel à la Lucas–Hopenhayn / Adamopoulos et al. (R1's old pt 4). **They never appeared in the paper** — R1's new pt 1 politely flags this. With §6.4 now removed from the main text, the clean resolution is:

- Add both discussions (2–3 paragraphs total) to the **online appendix** section that receives the moved §6.4 material:
  - *(a)* Note that with large manufacturing capital, MP_L is approximately constant, wages become effectively exogenous, and enclosure incentives operate purely through land rents — the qualitative dichotomy of Prop. 1 is unchanged though wage feedback is muted.
  - *(b)* Note that heterogeneous ability + occupational choice would add a selection margin (who encloses/manages vs. supplies labor), likely amplifying productivity effects of enclosure; cite Adamopoulos–Brandt–Leight–Restuccia (2022, 2024).
- In the **cover letter**, state plainly: "R1 correctly notes that discussions promised in our previous response did not appear in §6.4. Since the editor asked us to remove §6.4 from the main text, we have moved that section to the online appendix and included both promised discussions there."

This turns an awkward miss into a tidy fix, honors the promise, and respects the editor's cut. **Do not** try to squeeze these into the main text.

### 2.2 R5 pt 2 — table of symbols / parameters ⭐ RECOMMEND

Cheap, and directly serves the accessibility concern shared by R2, R5, and the editor. Suggested: a compact table near the end of Section 2 or start of Section 3:

| Symbol | Meaning | Key thresholds |
|--------|---------|----------------|
| $A$, $\theta$ | Baseline TFP; TFP gain on enclosed land ($\theta = A_e/A_c$) | $\theta_H = 1/\alpha$ separates complements/substitutes |
| $\alpha$ | Labor share (Cobb–Douglas) | — |
| $\bar l = \bar L/\bar T$ | Population density | Loci $\bar l_0^1, \bar l_1^1, \bar l_0^d, \bar l_1^d, \bar l_{gg}^d, \bar l^s, \dots$ |
| $c$ | Enclosure cost per unit land | Enters all loci as $c/A$ |
| $t_e, l_e$ | Shares of land, labor in enclosed sector | — |
| $\mu \in [0,1]$ | Community capacity to regulate commons access | $\mu=1$: no misallocation; $\theta_H^\mu = \frac{1}{\alpha} - \mu\frac{1-\alpha}{\alpha}$ |
| $\tau \in [0,1]$ | Compensation/resistance power of customary users | $\tau=1$: "trade"; $\tau=0$: "raid" |

(Format as a proper LaTeX table; consider adding a brief "where defined" column with equation numbers.)

### 2.3 R5 pt 3 — figure elucidation ⭐ RECOMMEND (light touch)

Do **not** restructure; just make each key figure self-contained:
- Figure 2 (`nash_eq.png`) caption: name what $\bar l_0^d$, $\bar l_1^d$, $\bar l_{gg}^d$ each mean in one clause.
- Figure 5 (`comparison.png`) caption: name all loci and the two hatched inefficiency regions (also fixes the R1 pt 3 confusion at its root — see 1.2).
- Figure 6 (`new_comp_fig4x4.png`): the panel-by-panel caption is already good; add one sentence identifying the blue dashed lines (see Phase 0 note).
- Figure 7 (`monopoly.png`): caption already references points A/B; fine.

One sentence per caption, no new figures needed beyond 1.4.

### 2.4 R1 pt 5 — collect all empirical discussions in one section: **DECLINE**

Reorganizing §6 at conditional-accept stage risks new inconsistencies for little gain; R1 explicitly says "totally up to you." The new trajectory figure (1.4) + the §6 overview paragraph already function as the collecting device. If desired, add one signposting sentence at the start of §6 noting that each subsection pairs a mechanism with its empirical literature.

### 2.5 R5 pts 1–2 — move game theory to an appendix: **DECLINE** (partially met)

The substance of the request (accessibility for economic historians / property-rights economists) is met by: the plain-language definitions (1.6), the parameter table (2.2), the trajectory figure (1.4), and caption improvements (2.3). Moving propositions/proofs out of the main text would be a major restructuring the editor did not ask for. State this reasoning in the cover letter if R5's points are mentioned.

### 2.6 R5 pt 4 — more economic history; ITQs/fisheries: OPTIONAL (one sentence max)

If desired, add a single sentence + citation in the Conclusion or §6 overview noting the framework extends beyond land — e.g., individual transferable quotas (ITQs) in ocean fisheries as a modern enclosure of a commons (cite e.g. Grafton, Squires & Fox 2000, or Costello, Gaines & Lynham 2008). Do not expand the historical case studies (English enclosures, U.S. frontier, colonial companies) — §6 is already the paper's longest section and the editor is pushing for tightening, not expansion.

### 2.7 Author addition — Holmström "budget breaker" framing of μ ⭐ RECOMMEND (author-initiated)

**Idea (JC):** Frame the μ = 0 commons as a budget-balanced average-product sharing rule — a **mirror image** of the team-production problem of Holmström (1982) — and the governance institution extracting share μ of possession rents as an *internal budget breaker* that absorbs the residual and realigns entry incentives. A genuine and revealing connection: it gives the tragedy of the commons a contract-theory pedigree and deepens the paper's existing "access fee" interpretation of μ.

**Making the allusion airtight.** A referee could object that Holmström is about *undersupply* of effort while the commons features *oversupply* of labor. The two are mirror images with a common cause, and the text should say so in one clause: under budget balance, a Holmström team member captures only a *fraction of the marginal* product of effort (→ effort undersupplied), while a commons entrant captures the *average* rather than the marginal product of labor (→ entry oversupplied). In both cases no budget-balanced sharing rule can align private and social returns at the relevant margin, and in both the remedy is a residual claimant who "breaks the budget."

**Placement:** §5.1 (`policy_regulate`), immediately after eq. (22) (`mu_move_intuition`) and its explanatory paragraph (~line 493), before "As governance improves (μ rises)…" (line 495). *(The originally drafted snippet targeted a §2.2 "Institutional parameters" / "Labor market governance (μ)" heading with an "unautomated sector" — that structure belongs to a different manuscript; the text below is the translation into this paper's structure and notation.)*

**Suggested LaTeX** (α = labor share in this paper, so the sharing weight is $(1-\mu(1-\alpha))$, *not* the $(1-\mu\alpha)$ of the original draft; the second equality uses the paper's Euler decomposition, eq. (8)):

```latex
The effective return to labor in the customary sector is
\begin{equation}
\label{eq:wc_mu}
\omega_c(\mu) \;=\; \mu \, MP_L^c + (1-\mu)\, AP_L^c
\;=\; \bigl(1-\mu(1-\alpha)\bigr)\, A \left(\frac{T_c}{L_c}\right)^{1-\alpha},
\end{equation}
where the second equality uses the decomposition in (\ref{commondecomp}). At
$\mu=0$, workers earn the full average product. This is a budget-balanced
sharing rule, and the resulting inefficiency is a mirror image of the
team-production problem of \citet{holmstrom1982}: there, budget balance
leaves each member with only a fraction of the marginal product of effort,
so effort is undersupplied; here, it awards each entrant the average rather
than the marginal product of labor, so entry is oversupplied. In both cases
no budget-balanced sharing rule can align private and social returns, and in
both the remedy is a residual claimant who breaks the budget. At $\mu=1$,
workers earn their marginal product and land rents accrue to the community
authority without distortion. For intermediate values, the governance
institution acts as precisely such an internal budget breaker: by extracting
a share $\mu$ of the possession rent from the labor-allocation game, it
absorbs the residual so that entrants' earnings move from average toward
marginal product, partially realigning entry incentives.\footnote{What is
essential is that the extracted rent not be returned contingent on deploying
labor in the commons: lump-sum redistribution to member households leaves
the allocative correction intact (see the first case analyzed in Section
\ref{labor_release}), whereas rebates proportional to commons participation
would restore average-product earnings and undo it. Holmström's requirement
that the budget breaker stand outside the team is the limiting case of this
condition. See \citet{baker2026} for a detailed treatment.}
```

**Notes / consistency checks:**
1. The new equation is exactly the closed form of eq. (22): $\omega_c(\mu) = MP_L^c + (1-\mu)\,MP_T^c\,T_c/L_c$, so no new derivation is needed — but verify the sentences around eq. (22) don't now read redundantly; the insertion can *replace* part of that explanation rather than duplicate it.
2. Symbol choice: eq. (22)'s surrounding text uses $w_c$ for $MP_L^c$; use a distinct symbol ($\omega_c(\mu)$ above, or $w_c^{\mathrm{eff}}$) to avoid a clash.
3. The factor $(1-\mu(1-\alpha))$ already appears in $\Lambda_\mu$ (eq. 25) and eq. (29) — after inserting, those passages read naturally as consequences of $\omega_c(\mu)$; consider adding "using (\ref{eq:wc_mu})" where $\Lambda_\mu$ is derived.
4. **Tension with §6.1 resolved by the footnote's contingency condition:** the paper's own redistribution case (§6.1, eq. 28) shows lump-sum rebates to members leave allocation governed by $\Lambda_\mu$ — so the binding requirement is only that rebates not be conditioned on commons participation, with Holmström's "outsider" as the limiting case. Residual caveat if wanted: the model fixes membership = total population; if membership itself were an entry margin (moving in to qualify for rebates), the distortion would reappear there.
5. Original draft said "capital's return" — changed to land rents.
6. **Bib entries needed** in `references.bib`:

```bibtex
@article{holmstrom1982,
  title={Moral hazard in teams},
  author={Holmstr{\"o}m, Bengt},
  journal={The Bell Journal of Economics},
  volume={13},
  number={2},
  pages={324--340},
  year={1982},
  publisher={The RAND Corporation}
}
```

   `baker2026` = a Baker working paper (companion piece): **entry still needed — add full title/venue details** before submission; biber will flag the unresolved key otherwise.
7. This is an addition beyond editor items (i)–(v) → **list it in the cover letter.**

---

## Phase 3 (not in current scope — for reference only)

- Draft the cover letter to Harstad: how (i)–(v) were addressed, plus an enumerated list of *all* additional changes made (Phase 0 items, 2.1, 2.2, 2.3, 2.7, and any of 2.6) — he explicitly requires this.
- Rebuild (`latexmk -pdf` with biber); text-diff old vs. new PDF to confirm only intended changes; check bibliography (Marx entry, holmstrom1982/baker2026, dropped 6.4 citations); update the online appendix site (https://open-enclose.github.io/) with the moved §6.4 + promised R1 discussions **before** submitting, since the paper's footnote points there.

---

## Quick-reference: what each referee gets

| Referee | Point | Action | Phase |
|---------|-------|--------|-------|
| R1 | 1 (missing promised discussions) | Move to online appendix w/ moved §6.4; explain in cover letter | 2.1 |
| R1 | 2 (abstract) | Rewrite long sentence; delete last sentence | 1.1 |
| R1 | 3 (first/second-best shading) | Verify figure; fix text/caption | 1.2 |
| R1 | 4 (τ in §5.2) | Move eq. (23) into §5.2 | 1.3 |
| R1 | 5 (collect empirics section) | Decline (politely) | 2.4 |
| R2 | trajectory figure | New labeled figure in §6 | 1.4 |
| R2 | remove §6.4 | Remove from main text → online appendix | 1.5 |
| R5 | 1 (parameter summary upfront) | Intro cross-ref to new figure + table | 1.4, 2.2 |
| R5 | 2 (appendix + symbol table) | Symbol table yes; restructuring no | 2.2, 2.5 |
| R5 | 3 (figure elucidation) | Caption sentences | 2.3 |
| R5 | 4 (more history, ITQs) | Optional single sentence | 2.6 |
| R5 | 5 (define strategic complements) | Plain definitions, intro + Prop. 1; demand/supply clarification | 1.6 |
| — | Authors (Holmström budget-breaker framing of μ) | Insert ω_c(μ) equation + mirror-image passage in §5.1 | 2.7 |
| — | Typos & notation found in our own read | Fix list | 0.1–0.11 |
