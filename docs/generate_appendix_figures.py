"""
Generate all figures for online appendix.
Saves figures to docs/Figures/ directory.

Usage:
    cd docs
    python generate_appendix_figures.py
"""

import sys
import os

# Add notebooks directory to path to import enclose module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'notebooks'))

try:
    from enclose import plotle, plotz, plotreq, plotmpts, allpart, threeplots
except ImportError as e:
    print(f"Error importing enclose module: {e}")
    print("Make sure notebooks/enclose.py exists and all dependencies are installed")
    sys.exit(1)

import matplotlib.pyplot as plt
import numpy as np

# Create output directory
output_dir = 'Figures'
os.makedirs(output_dir, exist_ok=True)

# Standard parameters for consistency
ALPHA = 2/3
C = 1.0
LBAR = 2.0
THETA = 1.5

print("Generating figures for online appendix...")
print("Parameters: theta={}, alpha={:.4f}, lbar={}, c={}".format(THETA, ALPHA, LBAR, C))
print("Output directory: {}/\n".format(output_dir))

# =============================================================================
# FIGURE 1: Output Function (after Equation 5)
# =============================================================================
def generate_fig1():
    """Output function z(t_e) - c*t_e showing optimal enclosure"""
    try:
        fig, ax = plt.subplots(figsize=(6, 4))
        plotz(th=THETA, alp=ALPHA, c=C, lbar=LBAR, ax=ax)
        ax.set_title('Output Function: z(t_e) - ct_e\n(theta={}, alpha={:.2f}, lbar={}, c={})'.format(
            THETA, ALPHA, LBAR, C), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'output_function.png')
        pdf_path = os.path.join(output_dir, 'output_function.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 1: Output function -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 1: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 2a: Labor Reaction - First-best only (after Equation 4)
# =============================================================================
def generate_fig2a():
    """Labor reaction function for first-best (mu=1)"""
    try:
        plotle(te=0.48, th=THETA, alp=ALPHA, mu=1)
        fig = plt.gcf()
        fig.set_size_inches(w=6, h=5)
        ax = fig.gca()
        ax.set_title('First-Best Labor Allocation: l_e^o(t_e) (mu=1)\n(theta={}, alpha={:.2f})'.format(
            THETA, ALPHA), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'labor_reaction_firstbest.png')
        pdf_path = os.path.join(output_dir, 'labor_reaction_firstbest.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 2a: Labor reaction (first-best, mu=1) -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 2a: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 2b: Labor Reaction - Comparison (after Equation 10)
# =============================================================================
def generate_fig2b():
    """Labor reaction function comparing open access and planner optimal"""
    try:
        plotle(te=0.48, th=THETA, alp=ALPHA, mu=0)
        fig = plt.gcf()
        fig.set_size_inches(w=6, h=5)
        ax = fig.gca()
        ax.set_title('Labor Allocation Wedge: Decentralized vs First-Best\n(theta={}, alpha={:.2f})'.format(
            THETA, ALPHA), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'labor_reaction_wedge.png')
        pdf_path = os.path.join(output_dir, 'labor_reaction_wedge.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 2b: Labor reaction (decentralized vs first-best) -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 2b: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 2c: Labor Reaction - Governance variations (after Equation 22)
# =============================================================================
def generate_fig2c():
    """Labor reaction function for different governance levels"""
    try:
        plotle(te=0.48, th=THETA, alp=ALPHA, mu=0)
        fig = plt.gcf()
        fig.set_size_inches(w=6, h=5)
        ax = fig.gca()
        ax.set_title('Labor Allocation with Governance: Different mu Values\n(theta={}, alpha={:.2f})'.format(
            THETA, ALPHA), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'labor_reaction_governance.png')
        pdf_path = os.path.join(output_dir, 'labor_reaction_governance.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 2c: Labor reaction (governance variations) -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 2c: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 3: Rental Rate Function (after Equation 12)
# =============================================================================
def generate_fig3():
    """Rental rate r(t_e) showing strategic complements/substitutes"""
    try:
        fig, ax = plt.subplots(figsize=(6, 4))
        plotreq(th=THETA, alp=ALPHA, lbar=LBAR, c=C, wplot=False, ax=ax)
        ax.set_title('Private Return to Enclosure: r(t_e)\n(theta={}, alpha={:.2f}, lbar={}, c={})'.format(
            THETA, ALPHA, LBAR, C), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'rental_rate.png')
        pdf_path = os.path.join(output_dir, 'rental_rate.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 3: Rental rate function -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 3: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 4: Parameter Space (after Equations 6-7)
# =============================================================================
def generate_fig4():
    """Parameter space showing threshold loci"""
    try:
        fig, ax = plt.subplots(figsize=(7, 5))
        allpart(c=C, alp=ALPHA, mu=0, soc_opt=True, cond_opt=True,
                pv_opt=True, pv_gg=False, logpop=True, ax=ax)
        ax.set_title('Enclosure Thresholds in Parameter Space\n(alpha={:.2f}, c={}, mu=0)'.format(
            ALPHA, C), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'parameter_space.png')
        pdf_path = os.path.join(output_dir, 'parameter_space.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 4: Parameter space and thresholds -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 4: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 5: Labor Market Misallocation (after Equation 18)
# =============================================================================
def generate_fig5():
    """Labor market diagram showing misallocation and deadweight loss"""
    try:
        fig, ax = plotmpts(te=0.4, alp=ALPHA, th=THETA, lbar=LBAR, mu=0)
        ax.set_title('Labor Market Misallocation and Efficiency Loss\n(t_e=0.4, theta={}, alpha={:.2f}, lbar={})'.format(
            THETA, ALPHA, LBAR), fontsize=11, fontweight='bold')
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'labor_misallocation.png')
        pdf_path = os.path.join(output_dir, 'labor_misallocation.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 5: Labor misallocation diagram -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 5: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# FIGURE 6: Comprehensive Three-Panel (Section 4.2)
# =============================================================================
def generate_fig6():
    """Three-panel figure showing complete picture"""
    try:
        threeplots(th=THETA, alp=ALPHA, c=C, lbar=LBAR,
                  soc_opt=True, cond_opt=True, pv_opt=True, pv_gg=False)
        fig = plt.gcf()
        fig.set_size_inches(w=12, h=8)
        fig.suptitle('Comprehensive Analysis: Parameter Space, Output Functions, and Returns\n(theta={}, alpha={:.2f}, lbar={}, c={})'.format(
            THETA, ALPHA, LBAR, C), fontsize=12, fontweight='bold', y=0.995)
        plt.tight_layout()

        png_path = os.path.join(output_dir, 'comprehensive.png')
        pdf_path = os.path.join(output_dir, 'comprehensive.pdf')
        fig.savefig(png_path, dpi=300, bbox_inches='tight')
        fig.savefig(pdf_path, bbox_inches='tight')
        plt.close(fig)
        print("[OK] Figure 6: Comprehensive three-panel figure -> {}".format(png_path))
        return True
    except Exception as e:
        print("[FAIL] Error generating Figure 6: {}".format(e))
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# Main execution
# =============================================================================
if __name__ == '__main__':
    results = []

    print("=" * 70)
    print("GENERATING MAIN FIGURES (6)")
    print("=" * 70)

    results.append(("Fig 1: Output function", generate_fig1()))
    results.append(("Fig 3: Rental rate", generate_fig3()))
    results.append(("Fig 4: Parameter space", generate_fig4()))
    results.append(("Fig 5: Labor misallocation", generate_fig5()))
    results.append(("Fig 6: Comprehensive", generate_fig6()))

    print("\n" + "=" * 70)
    print("GENERATING LABOR REACTION VARIATIONS (3)")
    print("=" * 70)

    results.append(("Fig 2a: Labor reaction (first-best)", generate_fig2a()))
    results.append(("Fig 2b: Labor reaction (wedge)", generate_fig2b()))
    results.append(("Fig 2c: Labor reaction (governance)", generate_fig2c()))

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    successful = sum(1 for _, success in results if success)
    total = len(results)

    print("\nGenerated: {}/{} figure sets successfully".format(successful, total))

    if successful == total:
        print("\n[OK] All figures saved to {}/".format(output_dir))
        print("  Total files: {} (PNG + PDF pairs)".format(successful * 2))
        print("\nNext steps:")
        print("  1. Update docs/online_appendix.md with figure references")
        print("  2. Run: quarto render docs/online_appendix.md --to pdf")
        print("  3. Verify figures appear correctly in online_appendix.pdf")
    else:
        print("\n[FAIL] {} figure(s) failed to generate".format(total - successful))
        print("  Check error messages above for details")
        sys.exit(1)
