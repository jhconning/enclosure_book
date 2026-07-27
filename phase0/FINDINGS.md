# Phase 0 Findings — figure discrepancy resolved

**Status: the main question is answered. No locus moved. All differences are axis-label text.**

Run on the office machine, 2026-07-27, from pre-snapshotted images (read-only — nothing was
regenerated, so nothing was overwritten).

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

## Remaining Phase 0 work (for the home machine)

The image comparison is done. Two items remain:

1. **Regenerate variant D** — run Matt's notebook today and confirm the current environment
   still reproduces the Feb 2026 figures. This tests environment drift, which the snapshot
   comparison can't. See `HANDOFF.md` §3.
2. **The `ltbar` / `tlbar` inversion** — a genuine code bug, independent of the figures.
   `req()` takes L̄/T̄ while `weq()` takes T̄/L̄, and `plotreq()` passes its single `tlbar`
   parameter positionally to both, so one is inverted whenever `tlbar ≠ 1`. Determine
   whether any paper figure was drawn through that path. See `HANDOFF.md` §4.

---

## Files here

| File | What it is |
|---|---|
| `compare_figures.py` | The comparison tool. Re-runnable; add variant D and re-run. |
| `snapshot/A_paper_2024/` | The paper's figures, as `main.tex` compiles them |
| `snapshot/B_appendix_committed/` | `open-enclose` HEAD versions |
| `snapshot/C_appendix_worktree/` | `open-enclose` uncommitted versions (pixel-identical to B) |
| `snapshot/D_regenerated/` | *(empty — to be filled on the home machine)* |
| `diffs/` | Side-by-side + difference heatmaps for each differing pair |
| `ylabel_A_vs_B.png` | The decisive crop: "population" vs "labor" density |
| `paper_ylabels_all.png` | All seven paper figures' y-labels stacked, showing the 3-way inconsistency |
