import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL("./libcode.so")

# Define argument and return types
lib.root1.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.root1.restype = ctypes.c_double

lib.root2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.root2.restype = ctypes.c_double

# Define the quadratic function
def quadratic_function(x):
    return 4 * x**2 + 4 * np.sqrt(3) * x + 3

# Wrapper to get roots from C
def quadratic_roots(a, b, c):
    x1 = lib.root1(a, b, c)
    x2 = lib.root2(a, b, c)
    return x1, x2

# Coefficients for 4x^2 + 4√3x + 3 = 0
a = 4
b = 4 * np.sqrt(3)
c = 3

# Generate x values
x_vals = np.linspace(-5, 2, 400)
y_vals = quadratic_function(x_vals)
y_zero = np.zeros_like(x_vals)

# Get roots from C
x1, x2 = quadratic_roots(a, b, c)

# Plotting
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=r'$4x^2 + 4\sqrt{3}x + 3$', color='blue')
ax.plot(x_vals, y_zero, color='gray', linewidth=1)

# Plot the double root (since x1 == x2)
ax.scatter(x1, 0, color="red", zorder=5, label=f'Root ({x1:.2f}, 0)')
ax.text(x1 + 0.2, 0.5, f'({x1:.2f}, 0)', fontsize=10, color="red")

# Final formatting
ax.grid(True)
ax.legend(loc="upper right")
ax.set_title("Graph of $4x^2 + 4\sqrt{3}x + 3$")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
