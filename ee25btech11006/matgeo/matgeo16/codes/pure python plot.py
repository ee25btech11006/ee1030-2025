import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the quadratic equation
a = 4
b = 4 * np.sqrt(3)
c = 3

# Define the quadratic function
def f(x):
    return a * x**2 + b * x + c

# Vertex (since discriminant = 0, vertex is the root)
x_root = -b / (2 * a)

# Generate x values around the root
x_vals = np.linspace(x_root - 4, x_root + 4, 400)
y_vals = f(x_vals)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r"$y = 4x^2 + 4\sqrt{3}x + 3$", color='blue')
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.axvline(0, color='black', linewidth=1)  # y-axis

# Highlight the root (double root)
plt.plot(x_root, 0, 'ro', label=fr"Root at $x = \frac{{-\sqrt{{3}}}}{{2}} \approx {x_root:.2f}$")

# Annotate the root
plt.annotate(fr"$x = \frac{{-\sqrt{{3}}}}{{2}}$", 
             xy=(x_root, 0), 
             xytext=(x_root + 1, 10),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')

# Labels and title
plt.title("Graph of $y = 4x^2 + 4\sqrt{3}x + 3$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("figs/fig.png)
plt.show()
