# Handoff — continuing on the home machine

**Written:** 2026-07-27, end of the office session.
**Purpose:** everything needed to resume the enclosures project on a different computer.

---

## 0. TL;DR — where things stand

**Phase 0's main question is already answered.** I ran the figure comparison before writing
this handoff, so you are not starting cold:

> The paper's 2024 figures and the appendix's 2026 figures differ **only in the y-axis label
> text** ("log population density" vs "log labor density"). No locus moved. The paper is
> economically correct. Full detail in [`phase0/FINDINGS.md`](phase0/FINDINGS.md).

Two Phase 0 items remain, both small — see §3 and §4 below.

**Everything is committed and pushed.** Nothing important lives only in a working tree.

---

## 1. The lay of the land — two repos, one goal

| | `enclosure_book` | `open-enclose.github.io` |
|---|---|---|
| Local path | `Y:\code\GitHub\enclosure_book` | `Y:\code\GitHub\open-enclose.github.io` |
| Remote | `github.com/jhconning/enclosure_book` | `github.com/open-enclose/open-enclose.github.io` |
| Site | `jhconning.github.io/enclosure_book/` | `open-enclose.github.io` |
| Toolchain | Jupyter Book v1 (sphinx, `_config.yml`/`_toc.yml`) | **mystmd** (`myst.yml`, `myst build --html`) |
| Contains | `enclose.py`, the paper (`paper/`), the math appendix, this handoff | Matt's `Model_Construction.ipynb`, the live appendix site |

These are **separate repos, siblings on disk, no shared git history**. Both are on the
Google-Drive-synced `Y:` mapping, so files sync — but git state syncs via GitHub, which is
why everything has been pushed (see §2).

**The destination** (agreed): one repo, published at `open-enclose.github.io`, with all
current code, reproducing every paper figure. `enclosure_book` eventually gets archived.

The full design proposal is in
[`REORGANIZATION_PROPOSAL.md`](REORGANIZATION_PROPOSAL.md) — read that first if you want the
architecture; read `phase0/FINDINGS.md` if you want to just finish Phase 0.

---

## 2. Getting the home machine current

Both repos are pushed and clean of anything important. On the home machine:

```bash
cd /y/code/GitHub/enclosure_book && git pull
cd /y/code/GitHub/open-enclose.github.io && git status
```

**Caution on the second one:** `open-enclose.github.io` has 6 figures showing as *modified*
in `git status`. I verified these are **pixel-identical to HEAD** — the byte differences are
PNG re-encoding only. They are safe to discard *or* keep; they carry no information. They are
also snapshotted at `phase0/snapshot/C_appendix_worktree/` regardless. Do **not** feel
obliged to commit them.

Because `Y:` is Google-Drive-synced, also confirm Drive has finished syncing before working —
otherwise you may see a half-synced tree that looks like phantom changes.

### Environment

Everything runs in the **`ecopy`** conda env (miniforge). On this office machine the
interactive `conda`/`mamba` shell hooks were not on PATH, so I invoked the env's python
directly. If `conda activate ecopy` works at home, just use it. Otherwise:

```bash
export PATH="$HOME/AppData/Local/miniforge3/envs/ecopy:$HOME/AppData/Local/miniforge3/envs/ecopy/Scripts:$PATH"
```

Required packages, all confirmed present in `ecopy` here — verify at home:

```bash
python -c "import numpy, matplotlib, sympy, PIL; print('ok')"
```

If anything is missing, install with **mamba** (not pip — per your standing preference):

```bash
mamba install -n ecopy -c conda-forge numpy matplotlib sympy pillow
```

For building the `enclosure_book` site you additionally need the **pinned** Jupyter Book:

```bash
mamba install -n ecopy -c conda-forge "jupyter-book=1.0.4.post1" pdoc
```

> **Why pinned:** upstream `jupyter-book` v2 is a completely different tool (mystmd-based,
> wants `myst.yml`) and cannot build `enclosure_book`'s classic `_config.yml`/`_toc.yml` site.
> `requirements.txt` now pins `1.0.4.post1`. Don't "upgrade" it.
>
> Note the irony worth keeping in mind: `open-enclose.github.io` *is* a real mystmd site, so
> it needs the Node-based `mystmd` CLI (`npm install -g mystmd`), not the Python package.

---

## 3. Remaining Phase 0, item 1 — regenerate variant D

**Question:** does today's environment still reproduce the Feb 2026 appendix figures, or has
matplotlib/sympy drift changed them? The snapshot comparison can't answer this.

**⚠️ Read before running:** Matt's notebook **saves over** `Figures/*.png` and
`social_opt_cond.png` in `open-enclose.github.io`. All existing variants are already
snapshotted under `phase0/snapshot/`, so nothing is truly at risk — but work on a copy
anyway so `git status` in that repo stays interpretable.

```bash
# from Y:\code\GitHub\enclosure_book\phase0
mkdir -p snapshot/D_regenerated

cd /y/code/GitHub/open-enclose.github.io
jupyter nbconvert --to notebook --execute --inplace Model_Construction.ipynb   # regenerates figures

# collect what it produced
cd /y/code/GitHub/enclosure_book/phase0
cp ../../open-enclose.github.io/Figures/*.png snapshot/D_regenerated/
cp ../../open-enclose.github.io/social_opt_cond.png snapshot/D_regenerated/

# re-run the comparison; it picks up D automatically
python compare_figures.py
```

Then restore the appendix repo if you don't want the regeneration:

```bash
cd /y/code/GitHub/open-enclose.github.io && git checkout -- Figures/ social_opt_cond.png
```

**Interpreting the result:** if `D vs B` is identical → the notebook is environment-stable,
good. If `D vs B` differs on *curves* → environment drift is changing the economics, which is
a genuine reproducibility problem and a strong argument for pinning versions in the merged
repo. If it differs only on text/margins → font availability differs between machines; note
it and move on.

---

## 4. Remaining Phase 0, item 2 — the `ltbar` / `tlbar` inversion

This is a **real code bug**, independent of the figures. In
[`notebooks/enclose.py`](notebooks/enclose.py):

```python
def req(te, th=1.0, alp=0.5, ltbar=1.0, mu=0.0):   # ltbar  = L̄/T̄
def weq(te, th=1.0, alp=0.5, tlbar=1.0, mu=0.0):   # tlbar  = T̄/L̄   <-- reciprocal!
```

and `plotreq()` has a single parameter named `tlbar` which it passes **positionally to both**:

```python
ax.plot(tte, req(tte, th, alp, tlbar), label=r'$r$')   # lands in req's `ltbar` slot
ax.plot(tte, weq(tte, th, alp, tlbar), label=r'$w$')   # lands in weq's `tlbar` slot
```

So one of the two curves is inverted whenever `tlbar ≠ 1`. `enclosure_model.ipynb` calls
`plotreq(th=2.2, alp=1/2, tlbar=0.16, ...)`.

**To determine:** (a) which of `req`/`weq` is the intended convention, (b) whether any figure
*in the paper* was produced through this path (the paper's `r_three_low.png` /
`r_three_high.png` three-panel figures are built from `plotreq` in `enclosure_model.ipynb`
cells 66–67 — but those filenames are **not** among the paper's seven `\includegraphics`, so
the exposure is probably limited to the website, not the paper). Confirm that.

`threeplots()` has the same issue: it calls `req(tte, th, alp, lbar)`, feeding an `lbar` into
the `ltbar` slot.

**Fix direction:** pick one density convention (recommend `lbar` = L̄/T̄ = population density,
matching the paper's `l̄`), rename throughout, and add an assertion or test. Do this in the
merged package rather than patching `enclose.py` in place, unless a paper figure turns out to
be affected — in which case fix it immediately.

---

## 5. What was done this session (context you may have lost)

Six commits on `enclosure_book`, all pushed:

| Commit | What |
|---|---|
| `2f4bb97` | Sync `enclose.py` + notebooks with the μ/τ extended model; regenerate pdoc Code API docs; pin `jupyter-book`, switch `pdoc3`→`pdoc` |
| `22daf01` | Temporary page (`notebooks/trajectories_temp.md`) sharing the new RESTUD trajectories figure with Matt, under a clearly-labeled "TEMP" TOC section |
| `0a59780` | `paper/final_revisions.md` — the phased guide for the RESTUD revision |
| `1581cb7` | Fix the deploy pipeline: HTML deploy was blocked by a pre-existing failing PDF build; also the pdoc step was unreachable due to shell `errexit` |
| `8008047` | Remove 62 orphaned tracked files (see `CLEANUP_INVENTORY.md`) |
| `8b8dd0d` | Fix two dead `_toc.yml` links + a Windows-backslash image path that 404'd on Linux CI |
| `18f0889` | Fix the site root redirecting to the Code API page instead of the homepage |

Plus this handoff, the Phase 0 work, and `REORGANIZATION_PROPOSAL.md`.

`jhconning.github.io/enclosure_book/` is currently live and healthy.

### Known-open items, not started

- **RESTUD revision proper** — `paper/final_revisions.md` has the full phased plan against
  the editor's required items (i)–(v). Untouched.
- **`paper/main.tex` and the submitted PDF are deliberately untracked** — you said the
  finalized paper gets placed later. They are on Drive, not in git.
- **Cleanup categories C** (`notebooks/code.md`, `notebooks/countour.ipynb` — current but
  unlinked from nav) and `references.md`/`references.bib` (orphaned but plausibly worth
  reviving as a References page). See `CLEANUP_INVENTORY.md`.
- **The PDF build still fails** in CI (pre-existing LaTeX/pgfplots `\omit` error). It is now
  non-blocking and visibly tracked rather than silently breaking deploys.

---

## 6. Suggested order of work at home

1. Skim [`phase0/FINDINGS.md`](phase0/FINDINGS.md) — 3 minutes, tells you Phase 0 is mostly done.
2. Do §3 (regenerate variant D) — ~15 minutes, mostly waiting on the notebook.
3. Do §4 (the `ltbar`/`tlbar` audit) — the one thing that could still touch the paper.
4. Decide the y-axis label wording ("population density" vs "labor density") and note it for
   the RESTUD revision, since three different wordings currently appear across the paper's
   seven figures.
5. Then either start Phase 1 of [`REORGANIZATION_PROPOSAL.md`](REORGANIZATION_PROPOSAL.md), or
   switch to the RESTUD revision itself via `paper/final_revisions.md`.

On the sequencing question the proposal raises (merge first vs revise first): my
recommendation is unchanged — do the merge's Phase 1 before finishing the revision,
specifically because `trajectories.png` is currently a third independent reimplementation of
the locus layer. Folding it in now stops the fragmentation from growing while the paper is
actively being edited.
