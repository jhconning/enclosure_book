# Online Appendix: Mathematical Derivations for Enclosure Paper

## Overview

The `online_appendix.md` file provides comprehensive mathematical derivations for the paper "Coordination, Enclosure, and the Commons." It is intended for readers who want to understand the detailed mathematical foundations of the main results.

**Current Status:** ✅ Complete with 4 illustrative figures
- File: `docs/online_appendix.md` (616+ lines)
- PDF Output: `online_appendix.pdf` (485 KB)
- Format: MyST Markdown (compatible with Jupyter Book and Quarto)

## Contents

### Structure
The appendix mirrors the main paper's organization:

```
- Section 3: Benchmark Model
  - Section 3.1: Technology and Resources
  - Section 3.2: First-Best Labor Allocation and Enclosure
  - Section 3.3: Decentralized Enclosure Processes
  - Section 3.4: Multiple Equilibria and Global Games

- Section 4: Social Efficiency of Private Enclosure
  - Section 4.1: The Second-Best Problem
  - Section 4.2: Sources of Inefficiency

- Section 5: The Extended Model
  - Section 5.1: The Regulated Commons
  - Section 5.2: Power and Compensation
  - Section 5.3: The Extended Wedge
  - Section 5.4: Second-Best Coordination

- Section G: Verification via Computational Implementation
  - G.1: Overview of Python Code
  - G.2: Key Function-to-Equation Mapping
  - G.3: Parameter Calibration Notes
  - G.4: Reproducibility Instructions
```

### Key Features

1. **Parameter A Consistency**
   - Base total factor productivity $A$ appears throughout
   - Composite form: $A\bar{l}^{\alpha}$ = potential output per unit land
   - Appears in all production functions, output expressions, and threshold formulas

2. **Numbered Equations**
   - All 34+ equations from the main paper are clearly labeled
   - Each equation includes cross-references to related results
   - Derivation steps shown explicitly

3. **Mathematical Derivations**
   - Detailed step-by-step proofs
   - All algebraic manipulations explained
   - Cobb-Douglas production function properties applied throughout

4. **Illustrative Figures** (4 key figures)
   - Output function dynamics
   - Parameter space threshold loci
   - Rental rate function and strategic effects
   - Labor market misallocation and deadweight loss

## Figures

### Generated Figures

Four key figures are included to enhance pedagogical value:

| Figure | Location | Purpose | Parameters |
|--------|----------|---------|------------|
| **Output Function** | After Eq. (5) | Shows $z(t_e) - c \cdot t_e$ | θ=1.5, α=2/3, l̄=2.0, c=1.0 |
| **Parameter Space** | After Eq. (6)-(7) | Threshold loci in (θ, ln l̄) space | α=2/3, c=1.0 |
| **Rental Rate** | After Eq. (12) | $r(t_e)$ showing strategic effects | θ=1.5, α=2/3, l̄=2.0, c=1.0 |
| **Labor Misallocation** | After Eq. (18) | MPL/APL diagram showing DWL | t_e=0.4, θ=1.5, α=2/3, l̄=2.0 |

**Figure Files:**
- Location: `docs/Figures/` directory
- Formats: PNG (300 dpi) and PDF (vector quality)
- Files:
  - `output_function.png` / `output_function.pdf`
  - `parameter_space.png` / `parameter_space.pdf`
  - `rental_rate.png` / `rental_rate.pdf`
  - `labor_misallocation.png` / `labor_misallocation.pdf`

### Parameters Used (Consistent Baseline)

All figures use the same baseline parameters to ensure consistency with main.tex diagrams:

```
θ (TFP gain in enclosed sector) = 1.5
α (labor share parameter) = 2/3
l̄ (population density) = 2.0
c (enclosure cost per unit land) = 1.0
A (base TFP) = 1.0
μ (governance parameter) = 0 (open access)
```

**Note:** θ = 1.5 > θ_H = 1/α = 1.5, so enclosure exhibits strategic substitutes.

## How to Regenerate the Appendix and Figures

### Prerequisites

```bash
# Required packages (should already be in conda environment)
- Python 3.7+
- matplotlib >= 3.1
- numpy >= 1.15
- scipy >= 1.0
```

### Step 1: Generate Figures

```bash
cd "h:\My Drive\code\GitHub\enclosure_book\docs"
python generate_appendix_figures.py
```

**Expected Output:**
```
Generating figures for online appendix...
Parameters: theta=1.5, alpha=0.6667, lbar=2.0, c=1.0
Output directory: Figures/

======================================================================
GENERATING MAIN FIGURES (6)
======================================================================
[OK] Figure 1: Output function -> Figures\output_function.png
[OK] Figure 3: Rental rate function -> Figures\rental_rate.png
[OK] Figure 4: Parameter space and thresholds -> Figures\parameter_space.png
[OK] Figure 5: Labor misallocation diagram -> Figures\labor_misallocation.png

[OK] All figures saved to Figures/
```

**Output Files:**
- 8 files created in `docs/Figures/` (4 PNG + 4 PDF pairs)
- Total size: ~500 KB

### Step 2: Render to PDF

```bash
cd "h:\My Drive\code\GitHub\enclosure_book"
quarto render docs/online_appendix.md --to pdf --output docs/online_appendix.pdf
```

**Expected Output:**
```
Rendering PDF
running lualatex - 1
  This is LuaHBTeX, Version 1.22.0 (TeX Live 2025)
  ...
Output created: online_appendix.pdf
```

**Output File:**
- `docs/online_appendix.pdf` (~485 KB)
- All figures embedded
- Fully cross-referenced

### Step 3: Verify

```bash
# Check that PDF was created and has reasonable size
ls -lh docs/online_appendix.pdf

# View the PDF in your PDF reader
# - All 4 figures should appear in correct locations
# - Captions should render properly
# - Math equations should display correctly
```

## File Organization

```
enclosure_book/
├── docs/
│   ├── online_appendix.md               # Main appendix source (MyST Markdown)
│   ├── online_appendix.pdf              # Generated PDF output
│   ├── online_appendix_rendered.pdf     # Earlier version (reference)
│   ├── APPENDIX_SUMMARY.txt             # Completion summary
│   ├── README_APPENDIX.md               # This file (documentation)
│   ├── main.tex                         # Main paper (LaTeX)
│   ├── Figures/                         # Generated figures directory
│   │   ├── output_function.png
│   │   ├── output_function.pdf
│   │   ├── parameter_space.png
│   │   ├── parameter_space.pdf
│   │   ├── rental_rate.png
│   │   ├── rental_rate.pdf
│   │   ├── labor_misallocation.png
│   │   └── labor_misallocation.pdf
│   ├── generate_appendix_figures.py     # Figure generation script
│   └── generate_essential_figures.py    # Simplified version
├── notebooks/
│   ├── enclose.py                  # Python implementation of model
│   ├── enclosure_model.ipynb       # Jupyter notebook with examples
│   └── labor_plot.ipynb            # Labor market visualization examples
└── ...
```

## Customizing Figures

### Change Parameters

Edit `docs/generate_appendix_figures.py` to modify baseline parameters:

```python
# Line 30-34: Standard parameters for consistency
ALPHA = 2/3        # Change labor share
C = 1.0            # Change enclosure cost
LBAR = 2.0         # Change population density
THETA = 1.5        # Change TFP gain
```

Then regenerate:
```bash
cd docs
python generate_appendix_figures.py
quarto render online_appendix.md --to pdf --output online_appendix.pdf
```

### Add More Figures

The `notebooks/enclose.py` module provides additional plotting functions:

```python
from enclose import plotle, plotz, plotreq, plotmpts, allpart, threeplots
```

Available functions:
- `plotle(te, th, alp, mu)` - Labor reaction function
- `plotz(th, alp, c, lbar, ax)` - Output function
- `plotreq(th, alp, lbar, c, wplot, ax)` - Rental rate
- `plotmpts(te, alp, th, lbar, mu)` - Labor misallocation
- `allpart(c, alp, mu, ...)` - Parameter space
- `threeplots(th, alp, c, lbar, ...)` - Comprehensive 3-panel figure

See `notebooks/enclose.py` for function signatures and examples.

## Key Mathematical Notation

| Symbol | Meaning | Domain |
|--------|---------|--------|
| $t_e$ | Share of land allocated to enclosed sector | $[0, 1]$ |
| $l_e$ | Share of labor allocated to enclosed sector | $[0, 1]$ |
| $A$ | Base total factor productivity | $> 0$ |
| $\bar{l}$ | Population density ($\bar{L}/\bar{T}$) | $> 0$ |
| $\alpha$ | Labor share in Cobb-Douglas | $(0, 1)$ |
| $\theta$ | TFP gain from enclosure (relative) | $> 0$ |
| $c$ | Enclosure cost per unit land | $> 0$ |
| $\Lambda_\mu$ | Labor intensity ratio | $> 0$ |
| $\theta_H$ | Critical threshold for strategic effects | $1/\alpha$ |
| $\mu$ | Governance/security parameter | $[0, 1]$ |
| $\tau$ | Compensation parameter | $[0, 1]$ |

## Troubleshooting

### Problem: Import error when running figure generation script

**Error:**
```
ImportError: No module named 'enclose'
```

**Solution:**
```bash
# Make sure you're running from docs directory
cd docs

# Verify enclose.py exists
ls ../notebooks/enclose.py

# Try again
python generate_appendix_figures.py
```

### Problem: Figures don't appear in PDF

**Check:**
1. Verify `docs/Figures/` contains PNG files
2. Check relative paths in `online_appendix.md` - should be `Figures/figure_name.png`
3. Run Quarto render again
4. Check for file permission issues

### Problem: PDF too large or rendering slowly

**Solutions:**
- Reduce DPI in `generate_appendix_figures.py` (change `dpi=300` to `dpi=150`)
- Generate fewer figures
- Use PDF format instead of PNG (smaller file size, vector quality)

## Integration with Jupyter Book

If publishing as a Jupyter Book:

```bash
# In project root
jupyter-book build .
```

The online appendix will be automatically included in the build if configured in `_toc.yml`:

```yaml
- file: docs/online_appendix.md
  title: Online Appendix
```

## Related Files

**For Understanding the Model:**
- `notebooks/enclose.py` - Complete Python implementation of the economic model
- `notebooks/enclosure_model.ipynb` - Jupyter notebook with interactive examples
- `notebooks/labor_plot.ipynb` - Detailed labor market diagrams

**For the Main Paper:**
- `docs/main.tex` - LaTeX source for the main paper
- `docs/main.pdf` - PDF version of the main paper

**Configuration:**
- `_config.yml` - Jupyter Book configuration
- `_toc.yml` - Table of contents for Jupyter Book

## Citation

When referring to derivations in the online appendix, use:

```
See Online Appendix, Equation (X), available at [URL]
```

Or for specific sections:

```
Following the analysis in Online Appendix, Section 3.2, we derive...
```

## Updates and Maintenance

### When to Regenerate

Regenerate figures and PDF if you:
- Change baseline parameter values
- Update equations in `online_appendix.md`
- Add new figures or sections
- Fix typos or clarifications

### Version Control

Recommended Git approach:

```bash
# Track source files
git add docs/online_appendix.md
git add docs/generate_appendix_figures.py
git add docs/README_APPENDIX.md

# Optionally track PDF (large file)
# git add online_appendix.pdf  # optional

# Don't track generated figures (can be regenerated)
# Add to .gitignore:
# docs/Figures/
```

## Future Enhancements

Potential additions to the appendix:

1. **More labor reaction plots** (after Equations 4, 22)
   - Show first-best vs. decentralized
   - Show governance parameter variation

2. **Comprehensive 3-panel figure** (Section 4.2)
   - Parameter space + output functions + returns

3. **Numerical examples**
   - Specific calibrations with numerical results
   - Sensitivity analysis

4. **Extended model figures**
   - Showing effects of $\mu$ (governance)
   - Showing effects of $\tau$ (compensation)

See `notebooks/enclose.py` for available plotting functions that could be added.

## Contact & Support

For questions about the appendix or figure generation:

1. Check the comments in `generate_appendix_figures.py`
2. Review function signatures in `notebooks/enclose.py`
3. See example usage in `notebooks/enclosure_model.ipynb`

---

**Last Updated:** January 30, 2025
**Appendix Version:** 2.0 (with figures)
**Python Version:** 3.7+
**Quarto Version:** 1.3+
