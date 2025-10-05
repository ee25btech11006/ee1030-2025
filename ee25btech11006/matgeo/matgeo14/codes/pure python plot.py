import numpy as np
import matplotlib.pyplot as plt
import os

# --- Define matrix form constants ---
V = np.eye(2)  # V = I

# Given circle: x^2 + y^2 = 9
u1 = np.array([[0], [0]])
f1 = -9

# Given points (as column vectors)
P = np.array([[0], [0]])
Q = np.array([[1], [0]])

# Step 1: Relation between u, P, Q
# (QᵀVQ - PᵀVP) + 2uᵀ(Q - P) = 0
lhs = (Q.T @ V @ Q - P.T @ V @ P)
diff = Q - P
u_T_diff = -lhs / 2
# Let u = [[u1], [u2]]
u1_val = -1/2  # from above condition

# Step 2: Tangency condition
# Internal touch: ||u|| = 3 - sqrt(uᵀu)
# Let sqrt(uᵀu) = k => k = 3 - k => k = 1.5
k = 3/2
# => uᵀu = 9/4 = u1^2 + u2^2
u2_val = np.sqrt(9/4 - u1_val**2)  # √2

# Two possible u vectors
u_pos = np.array([[u1_val], [u2_val]])
u_neg = np.array([[u1_val], [-u2_val]])

# Step 3: Circle parameters
def circle_params(u):
    f = -2 * (u.T @ P) - (P.T @ V @ P)
    c = -u
    r = np.sqrt(float(u.T @ u - f))
    return c, r

# Given circle
c1, r1 = np.array([[0], [0]]), 3
c2_pos, r2_pos = circle_params(u_pos)
c2_neg, r2_neg = circle_params(u_neg)

# --- Plot helper ---
def plot_circle(ax, c, r, label, color, text_label):
    theta = np.linspace(0, 2*np.pi, 400)
    circle = c + r * np.vstack((np.cos(theta), np.sin(theta)))
    ax.plot(circle[0, :], circle[1, :], color=color, label=label)
    ax.scatter(c[0], c[1], color=color, marker='o')
    ax.text(float(c[0])+0.15, float(c[1])+0.15, text_label, color=color, fontsize=10)

# --- Plot ---
fig, ax = plt.subplots(figsize=(6,6))
plot_circle(ax, c1, r1, "Given Circle", 'blue', r'$C_1(0,0)$')
plot_circle(ax, c2_pos, r2_pos, "Req. Circle 1", 'red', r'$C_2(\frac{1}{2},\sqrt{2})$')
plot_circle(ax, c2_neg, r2_neg, "Req. Circle 2", 'green', r'$C_3(\frac{1}{2},-\sqrt{2})$')

# Plot points P and Q
ax.scatter(P[0], P[1], color='black')
ax.text(P[0]+0.05, P[1]-0.25, r'$P(0,0)$', color='black', fontsize=10)
ax.scatter(Q[0], Q[1], color='black')
ax.text(Q[0]+0.05, Q[1]-0.25, r'$Q(1,0)$', color='black', fontsize=10)

# --- Graph settings ---
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title(r'Circle Touching $x^2 + y^2 = 9$ and Passing through $P, Q$')

# --- Save figure for Overleaf ---
os.makedirs("figs", exist_ok=True)
plt.savefig("figs/Figure_1.png", dpi=300, bbox_inches='tight')

plt.show()