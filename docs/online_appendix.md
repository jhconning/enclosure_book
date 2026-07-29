# Online Appendix — moved

This file used to hold the full mathematical appendix, ~1,400 lines covering equations
(1)–(43). **It was a second copy of the same document that ships with the site**, and on
2026-07-29 the two silently diverged: work on §6.4 landed here while the site's copy still
carried a stale stub. They were reconciled by hand, which is not a process that survives
repetition.

The canonical copy is now the site's, which is also what the paper's own footnote points
readers to:

> **`open-enclose.github.io/content/04-derivations.md`**
> published at <https://open-enclose.github.io/>

## Why the site owns it

The paper describes the online appendix as *being* that site. Keeping an editable second
copy in this repository created two ways to change one document, with nothing to detect a
divergence. A pointer cannot diverge.

## Where the content went

Nothing was lost. The full text is in the site repository, and this file's own history is
intact — `git log --follow docs/online_appendix.md` recovers every version, including the
final one at commit `37ee9bf` immediately before this replacement.

## Stale references

Several files in this repository still refer to `docs/online_appendix.md` by path —
`README_APPENDIX.md`, `generate_appendix_figures.py`, `REORGANIZATION_PROPOSAL.md`,
`APPENDIX_PLAN.md`, and notes under `notes/`. They were left pointing here deliberately, so
that following any of them lands on this notice rather than on a missing file. Read them as
pointing to the site copy.
