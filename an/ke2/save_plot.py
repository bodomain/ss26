import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-2.5, 2.5, 1000)
sqrt2 = np.sqrt(2)

# Define the step function (as if defined on all reals; actual domain is only rationals)
y = np.where(np.abs(x) < sqrt2, 0, 1)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2, label=r'$f(x)=0$ for $|x|<\sqrt{2}$, $f(x)=1$ for $|x|>\sqrt{2}$')

# Vertical dashed lines at the irrational boundaries
plt.axvline(x=-sqrt2, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=sqrt2, color='gray', linestyle='--', alpha=0.7)

# Open circles to indicate points not in the domain (x = ±√2 are irrational)
plt.plot(-sqrt2, 0, 'wo', markeredgecolor='black', markersize=8)
plt.plot(-sqrt2, 1, 'wo', markeredgecolor='black', markersize=8)
plt.plot(sqrt2, 0, 'wo', markeredgecolor='black', markersize=8)
plt.plot(sqrt2, 1, 'wo', markeredgecolor='black', markersize=8)

# Labels, title, grid, legend
plt.xlabel(r'$x$ (only rational numbers are in the domain)', fontsize=12)
plt.ylabel(r'$f(x)$', fontsize=12)
plt.title(r'Function $f:\mathbb{Q}\to\mathbb{R}$ with $f(x)=0$ if $x^2<2$, $f(x)=1$ if $x^2>2$', fontsize=14)
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1])
plt.grid(alpha=0.3)
plt.legend(loc='upper left')

# Explanation note
plt.text(0, -0.15, 'Note: Only rational $x$ are considered; the lines show the value at all rational $x$.',
         ha='center', fontsize=10, style='italic')

plt.tight_layout()
# Save as PDF for high-quality inclusion in LaTeX
plt.savefig('figures/f_plot.pdf', dpi=300, bbox_inches='tight')
print('Saved figure to figures/f_plot.pdf')
