# Tasks

## Active

- [ ] **Add the coordination sentence to the paper — in Overleaf** - enclosure paper, §\ref{manuf_sec}
  - Deliberately *not* written by Claude on 2026-07-29 — manuscript edits are yours.
  - **Edit in Overleaf, not in this repo.** `paper/main.tex` and `docs/main.tex` here are stale local exports (2026-02-13 and 2026-02-06); Overleaf is the source of truth, backed to Dropbox, and kept isolated on purpose. Editing the local copies would create a fork.
  - **Where:** the closing paragraph of `\subsection{Structural transformation and manufacturing}`, currently the vague *"Depending on initial conditions, the economy may experience a smooth and efficient transformation, become stuck with excessive labor in the customary sector, or undergo premature or excessive enclosure and structural change."* Replace or sharpen it. (For reference the paragraph sits at `paper/main.tex:717` in the stale export.)
  - **Why there:** the section opens by promising *"we identify the conditions that trigger regime changes and the general equilibrium feedbacks that shape their timing and extent"* — and never delivers it. This cashes that promise, at the point where the paper already reaches for the claim and comes up short.
  - **Draft text:**
    > The condition under which enclosure releases labor to manufacturing is the same condition under which enclosure decisions are strategic complements: both hold precisely when $\Lambda_\mu < 1$, that is, when $\theta < \theta_H^\mu$. The enclosures most consequential for industrialization are therefore exactly those whose extent is not pinned down by fundamentals alone — which may help explain why enclosure arrived in waves, and why regions with similar endowments experienced it so differently.
  - **Optional second touch:** line ~730 in the Conclusion already says *"In low-productivity or weak-governance environments, enclosure decisions become strategic complements."* Appending "—which is also, precisely, the region in which enclosure releases labor to industry" costs a clause and closes the loop.
  - **Preferred over** the three-regime taxonomy considered earlier: uses machinery the paper already has, introduces no new notation, claims more.
  - **Backing:** `docs/online_appendix.md` §6.4 eq. (41) and the remark following it; derivation verified numerically (signs of $\partial l_m/\partial t_e$ and $dr/dt_e$ agree at every $\theta$ tested). Full argument in `notes/manuf_paper_ideas.md` §1.

## Waiting On

## Someday

## Done
