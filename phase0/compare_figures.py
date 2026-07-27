"""
Phase 0: determine whether the paper's figures differ from the online
appendix's figures cosmetically or substantively.

Compares up to four variants of each figure:

  A  paper/Figures/                  dated 2024-07-18  -- what main.tex compiles
  B  open-enclose HEAD               dated 2026-02-07  -- last committed appendix version
  C  open-enclose working tree       dated 2026-02-07  -- UNCOMMITTED regeneration
  D  freshly regenerated (optional)  -- what the notebook produces today

A/B/C are pre-snapshotted in phase0/snapshot/ so they cannot be destroyed by
re-running the notebook. Put a fresh regeneration in phase0/snapshot/D_regenerated/
to include it in the comparison.

Usage (from phase0/):
    python compare_figures.py            # compare + write diff images
    python compare_figures.py --no-diff  # table only, no image output

Output:
    - a summary table to stdout
    - phase0/diffs/<figure>__<X>_vs_<Y>.png  side-by-side + difference heatmap

Reading the results
-------------------
Identical dimensions + near-zero difference  -> byte-level re-save only.
Identical dimensions + differences confined
  to text/label areas                        -> cosmetic (fonts, offsets, labels).
Differences along curve paths                -> A LOCUS MOVED. Substantive.
                                                Escalate: this affects the paper.
Different dimensions                         -> figsize/dpi changed; inspect the
                                                side-by-side visually, since pixel
                                                metrics are not meaningful.
"""

from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
SNAP = HERE / "snapshot"
DIFFS = HERE / "diffs"

VARIANTS = {
    "A": ("A_paper_2024", "paper 2024-07-18 (what main.tex compiles)"),
    "B": ("B_appendix_committed", "appendix HEAD 2026-02-07 (committed)"),
    "C": ("C_appendix_worktree", "appendix worktree 2026-02-07 (uncommitted)"),
    "D": ("D_regenerated", "regenerated today"),
}


def load(path: Path) -> np.ndarray | None:
    """Load a PNG as float RGB in [0,1], dropping alpha by compositing on white."""
    if not path.exists():
        return None
    im = Image.open(path).convert("RGBA")
    arr = np.asarray(im).astype(float) / 255.0
    rgb, alpha = arr[..., :3], arr[..., 3:4]
    return rgb * alpha + (1.0 - alpha)  # composite on white


def compare(a: np.ndarray, b: np.ndarray) -> dict:
    """Pixel statistics for two same-shaped images."""
    diff = np.abs(a - b).max(axis=2)  # worst channel per pixel
    changed = diff > 0.02  # ~5/255, ignores antialiasing jitter
    return {
        "max": float(diff.max()),
        "mean": float(diff.mean()),
        "pct_changed": 100.0 * changed.mean(),
        "n_changed": int(changed.sum()),
        "diff": diff,
        "changed": changed,
    }


def write_diff_image(name: str, ka: str, kb: str, a: np.ndarray, b: np.ndarray, st: dict) -> Path:
    DIFFS.mkdir(exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(21, 7))
    axes[0].imshow(a); axes[0].set_title(f"{ka}: {VARIANTS[ka][1]}", fontsize=10)
    axes[1].imshow(b); axes[1].set_title(f"{kb}: {VARIANTS[kb][1]}", fontsize=10)
    im = axes[2].imshow(st["diff"], cmap="inferno", vmin=0, vmax=max(st["max"], 1e-6))
    axes[2].set_title(
        f"difference  (max={st['max']:.3f}, {st['pct_changed']:.2f}% of pixels)", fontsize=10
    )
    fig.colorbar(im, ax=axes[2], fraction=0.046)
    for ax in axes:
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle(name, fontsize=13)
    fig.tight_layout()
    out = DIFFS / f"{Path(name).stem}__{ka}_vs_{kb}.png"
    fig.savefig(out, dpi=90, bbox_inches="tight")
    plt.close(fig)
    return out


def main(write_diffs: bool = True) -> int:
    figures = sorted({p.name for k, _ in VARIANTS.values() for p in (SNAP / k).glob("*.png")})
    if not figures:
        print(f"No figures found under {SNAP}", file=sys.stderr)
        return 1

    print(f"\nPhase 0 figure comparison\nsnapshot: {SNAP}\n")
    print("Variants present:")
    for key, (sub, desc) in VARIANTS.items():
        d = SNAP / sub
        n = len(list(d.glob("*.png"))) if d.exists() else 0
        print(f"  {key}  {desc:<52} {n} figure(s)")

    verdict_rows = []
    for name in figures:
        loaded = {}
        for key, (sub, _) in VARIANTS.items():
            img = load(SNAP / sub / name)
            if img is not None:
                loaded[key] = img
        if len(loaded) < 2:
            only = next(iter(loaded), "-")
            print(f"\n{name}\n  only present in variant {only} -- nothing to compare")
            verdict_rows.append((name, f"only in {only}", "-"))
            continue

        print(f"\n{name}")
        for key, img in loaded.items():
            h, w, _ = img.shape
            print(f"  {key}: {w} x {h} px")

        for ka, kb in combinations(sorted(loaded), 2):
            a, b = loaded[ka], loaded[kb]
            if a.shape != b.shape:
                print(f"  {ka} vs {kb}: DIMENSIONS DIFFER -> compare visually, not by pixels")
                verdict_rows.append((name, f"{ka}v{kb}", "dims differ"))
                continue
            st = compare(a, b)
            if st["n_changed"] == 0:
                tag = "identical"
            elif st["pct_changed"] < 0.5:
                tag = "near-identical"
            elif st["pct_changed"] < 5:
                tag = "MINOR - inspect"
            else:
                tag = "MAJOR - inspect"
            print(
                f"  {ka} vs {kb}: {tag:<16} "
                f"{st['pct_changed']:6.2f}% pixels changed, max delta {st['max']:.3f}"
            )
            verdict_rows.append((name, f"{ka}v{kb}", f"{tag} ({st['pct_changed']:.2f}%)"))
            if write_diffs and st["n_changed"] > 0:
                out = write_diff_image(name, ka, kb, a, b, st)
                print(f"      -> {out.relative_to(HERE)}")

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    for name, pair, verdict in verdict_rows:
        print(f"  {name:<26} {pair:<10} {verdict}")
    print(
        "\nNext: open the diff images. If the changed pixels lie on CURVES, a locus\n"
        "moved and this is substantive (affects the paper). If they lie on TEXT or\n"
        "at the margins, it is cosmetic (fonts/offsets/labels).\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(write_diffs="--no-diff" not in sys.argv))
