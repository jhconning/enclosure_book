# Phase 0 Findings — figure discrepancy resolved

**Status: Phase 0 is complete.** No locus moved. All differences are axis-label text. Today's
environment reproduces the figures exactly (no drift). The `ltbar`/`tlbar` code bug is fixed.

Started on the office machine, 2026-07-27, from pre-snapshotted images (read-only). Finished
on the home machine, 2026-07-28: variant D regenerated, and the `ltbar`/`tlbar` inversion and
`totalq` θ double-count fixed in `enclose.py`.

---

## The verdict

### 1. Cosmetic, not substantive — the paper's figures are economically correct

All pixel differences between the paper's 2024 figures and the appendix's 2026 figures are
confined to **exactly 4,503 pixels in a 32-px-wide strip at x[83–114]** — the left margin,
where the rotated y-axis label sits. Identical pixel count, identical bounding box, in all
three affected figures. No curve, no locus, no shaded region differs anywhere.

| Figure | A (paper 2024) vs B (appendix 2026) |
|---|---|
| `comparison.png` | **identical** |
| `new_comp_fig4x4.png` | **identical** |
| `monopoly.png` | 0.56% — y-axis label only |
| `nash_so_comp.png` | 0.56% — y-axis label only |
| `social_opt_cond.png` | 0.56% — y-axis label only |
| `social_optimum.png`, `nash_eq.png` | only exist in the paper (they come from `enclose.py`, not Matt's notebook) |

**The actual difference** (see `ylabel_A_vs_B.png`):

- **Paper (2024):** `ln(l̄) (log population density)`
- **Appendix (2026):** `ln(l̄) (log labor density)`

Matt changed the wording in Feb 2026; it never propagated back to the paper.

### 2. The "uncommitted changes" scare was nothing

`open-enclose.github.io` has 6 figures showing as modified in `git status`. They are
**pixel-identical to HEAD** — byte differences are PNG re-encoding/metadata only. Nothing
was at risk, and nothing needs recovering. (They're still snapshotted, for safety.)

### 3. Bonus finding — the paper is internally inconsistent about this label

Extracting the y-axis label from all seven paper figures (`paper_ylabels_all.png`) shows
**three different conventions in the published set**:

| Wording | Figures |
|---|---|
| `ln(l̄) (log population density)` | `social_optimum`, `nash_eq`, `nash_so_comp`, `social_opt_cond`, `monopoly` |
| `ln(l̄)` — bare, no descriptor | `comparison.png` (paper Figure 5) |
| `ln(l̄) (log pop. dens.)` — abbreviated | `new_comp_fig4x4.png` (paper Figure 6, the 2×2) |

This is visible to a referee and worth fixing in the RESTUD revision.

**Decided, 2026-07-28: standardize on "log population density."** Matches the paper's
existing prose and 5 of 7 figures already, so only the two outlier figure labels need
changing — no text edits. Tracked as item 0.12 in `paper/final_revisions.md`.

**Note on terminology:** `l̄ = L̄/T̄` is labor per unit land. The paper's *text* says
"population density" consistently (§3.1, and the Figure 1/2 captions). So the paper's text
and its 2024 figures agree; the 2026 appendix is the outlier. Choosing "population density"
requires no text edits; choosing "labor density" means updating the paper's prose too.

---

## What this means for the plan

- **Not urgent for the paper's correctness.** The figures are economically identical; this
  does not block the RESTUD revision, and no result changes.
- **Worth one small cleanup in the revision:** pick one wording, apply it to all eight
  figures (including the new `trajectories.png`), and confirm the paper's prose matches.
- **The reproducibility gap is real but narrower than feared:** the appendix genuinely does
  reproduce the paper's figures, modulo a label string.
- **This strengthens the case for the merge:** a single `style.py` with one `common_labels()`
  would have made a three-way label inconsistency impossible.

---

## Remaining Phase 0 work

~~1. **Regenerate variant D**~~ — **done, 2026-07-28.** See below.
~~2. **The `ltbar` / `tlbar` inversion**~~ — **done, 2026-07-28.** See below.

**Phase 0 is complete.**

---

## Variant D (regenerated today) — resolved

Re-executed `open-enclose.github.io/Model_Construction.ipynb` under `ecopy` (its saved
kernelspec, `conda-base-py`, isn't registered on this machine — ran with
`--ExecutePreprocessor.kernel_name=ecopy` instead) and collected the output into
`snapshot/D_regenerated/`.

**Result: `B vs D` is identical (0.00% pixels changed) on every figure.** Today's environment
reproduces the Feb 2026 committed appendix figures exactly — no matplotlib/sympy drift.
`A vs D` reproduces the same 0.56%, label-only differences already established as cosmetic
(§1 above). The appendix repo's working tree was restored to clean afterward
(`git checkout -- Figures/ social_opt_cond.png Model_Construction.ipynb`); nothing here needed
to persist since the snapshot already captures the result.

**Conclusion:** the reproducibility gap is closed. The appendix notebook, run today, produces
the paper's figures bit-for-bit (modulo the known label wording). No environment pinning is
needed to fix a drift problem, because there isn't one — though pinning remains good practice
for the merge regardless.

---

## The `ltbar` / `tlbar` inversion — resolved

**No paper figure was affected.** Both production routes for the seven `\includegraphics` in
`main.tex` were checked: five come from Matt's `Model_Construction.ipynb`, which imports only
numpy/sympy/matplotlib and never touches `enclose.py`; `social_optimum.png` and `nash_eq.png`
come from `allpart`, which computes the loci in closed form and takes **no density argument at
all** (density is the y-axis). `r_three_low.png` / `r_three_high.png` are not in the paper.

**The intended convention is `l̄ = L̄/T̄`**, per `main.tex` §2 and the rental expression
`r = θ(1-α)·A·l̄^α·(…)`. So `req` was right and the `weq` / `mple` / `aple` / `mpt` family were
written against the reciprocal `t̄ = T̄/L̄`.

**The notebook's numbers were already `l̄`; only the parameter name was wrong.**
`plotreq(th=2.2, alp=1/2, lbar=0.16/0.19/0.24, c=0.5)` gives `r(0) = 0.484 / 0.527 / 0.593`
against `c = 0.5` — three panels deliberately straddling the threshold. Read as `T̄/L̄` they
would imply `l̄ = 6.25` and `r(0) ≈ 3.0 ≫ c`, a degenerate figure.

**Fix applied:** `enclose.py` now takes `lbar` everywhere; `plotreq` passes it by keyword to
both curves. `tests/test_enclose.py` pins the invariants that the two conventions were hiding
(`req == mpt` at `l_e(t_e)`; `weq == mple` at μ=0; `r ∝ l̄^α` vs `w ∝ l̄^{α-1}`).

**Figure impact, verified pixel-by-pixel:** `r_three_low.png`, `r_three_high.png`,
`z_three.png` and the appendix's `output_function` / `parameter_space` / `rental_rate` are all
**identical**. Only `docs/Figures/labor_misallocation.png` changed (4.74% of pixels) — the
`plotmpts` call in `generate_appendix_figures.py` that had been reading `LBAR = 2.0` as `T̄/L̄`
while the same constant meant `l̄` in the two other figures of that script.

**Update, 2026-07-28:** both since fixed ahead of the merge. `totalq` double-counted θ
(`th * f(te, leq, alp, th)`, where `f` already multiplies by θ) — corrected, with a test
pinning `totalq(te, ..., mu=1) == z(te, ...)`. The bug was latent: `totalq`'s only call site
(`plotY`'s `axhline`) always evaluates at `t_e=0`, where `l_e=0` makes the affected term zero
regardless of the bug, and `plotY` itself is never invoked from any notebook or figure-generation
script — so no figure or notebook output changed. `notebooks/enclose2.py`, a stale duplicate
carrying both this defect and the original `tlbar`/`ltbar` naming bug, has been deleted (it was
untracked, had zero importers anywhere in the repo, and its "brings μ/τ into all functions"
header comment was aspirational — τ never appears in either file).

---

## Files here

| File | What it is |
|---|---|
| `compare_figures.py` | The comparison tool. Re-runnable; add variant D and re-run. |
| `snapshot/A_paper_2024/` | The paper's figures, as `main.tex` compiles them |
| `snapshot/B_appendix_committed/` | `open-enclose` HEAD versions |
| `snapshot/C_appendix_worktree/` | `open-enclose` uncommitted versions (pixel-identical to B) |
| `snapshot/D_regenerated/` | Regenerated 2026-07-28, `ecopy` kernel — identical to B |
| `diffs/` | Side-by-side + difference heatmaps for each differing pair |
| `ylabel_A_vs_B.png` | The decisive crop: "population" vs "labor" density |
| `paper_ylabels_all.png` | All seven paper figures' y-labels stacked, showing the 3-way inconsistency |
