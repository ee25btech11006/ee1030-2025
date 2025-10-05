import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Points A and B
A = np.array([3, 4, 1])
B = np.array([5, 1, 6])

# Direction vector
m = B - A

# Intersection with XY-plane
lambda_val = -A[2] / m[2]
intersection = A + lambda_val * m

# Convert to fractions for labeling
def to_frac(vec):
    return [Fraction(x).limit_denominator() for x in vec]

A_frac = to_frac(A)
B_frac = to_frac(B)
intersection_frac = to_frac(intersection)

# Extend line further for a clean look
lambdas = np.linspace(-1.5, 2.0, 300)
line_points = np.array([A + l * m for l in lambdas])

# Plotting
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Extended line
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], 'b--', label='Line AB')

# Points
ax.scatter(*A, color='red', s=20, marker='o')
ax.scatter(*B, color='green', s=20, marker='o')
ax.scatter(*intersection, color='purple', s=20, marker='o')

# Annotate points with fractions, keep original format but adjust offsets
ax.text(A[0]+0.4, A[1]+0.2, A[2]+0.4, 
        f"A({A_frac[0]},{A_frac[1]},{A_frac[2]})", color='red', fontsize=10)

ax.text(B[0]+0.2, B[1]+0.2, B[2]+0.2, 
        f"B({B_frac[0]},{B_frac[1]},{B_frac[2]})", color='green', fontsize=10)

ax.text(intersection[0]+1.0, intersection[1]-0.5, intersection[2]+0.3, 
        f"X({intersection_frac[0]},{intersection_frac[1]},{intersection_frac[2]})", color='purple', fontsize=10)

# XY-plane
xx, yy = np.meshgrid(np.linspace(0,8,10), np.linspace(0,8,10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray')

# Axes labels, grid, title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Extended Line AB intersecting XY-plane')
ax.legend()
ax.grid(True)

# Adjust viewing window for clarity
ax.set_xlim(0,8)
ax.set_ylim(0,8)
ax.set_zlim(-1,8)

plt.show()