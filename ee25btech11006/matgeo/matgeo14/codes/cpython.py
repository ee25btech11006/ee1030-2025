import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared C library
lib = ctypes.CDLL("./libcode.so")

# Define function signatures
lib.find_radius.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.find_radius.restype = ctypes.c_double

lib.find_f.argtypes = [ctypes.c_double]
lib.find_f.restype = ctypes.c_double

# Given circle: x^2 + y^2 = 9
r1 = 3.0
C1 = np.array([0.0, 0.0])

# Required circle parameters from code.c logic
g = -0.5
c = 0.0

# Get f and -f from C function
f = lib.find_f(g)
f_neg = -lib.find_f(g)

# Centers of required circles
C2 = np.array([-g, -f])
C3 = np.array([-g, -f_neg])

# Radii (same for both)
r2 = lib.find_radius(g, f, c)
r3 = r2

# Generate points for circles
theta = np.linspace(0, 2*np.pi, 400)

# Circle 1: Given circle x^2 + y^2 = 9
circle1_x = C1[0] + r1*np.cos(theta)
circle1_y = C1[1] + r1*np.sin(theta)

# Circle 2: Required circle (upper)
circle2_x = C2[0] + r2*np.cos(theta)
circle2_y = C2[1] + r2*np.sin(theta)

# Circle 3: Required circle (lower)
circle3_x = C3[0] + r3*np.cos(theta)
circle3_y = C3[1] + r3*np.sin(theta)

# Plot
fig, ax = plt.subplots()

# Given circle
ax.plot(circle1_x, circle1_y, color="blue", label=r"$x^2 + y^2 = 9$")

# Required circles
ax.plot(circle2_x, circle2_y, color="red", label="Required Circle 1")
ax.plot(circle3_x, circle3_y, color="green", label="Required Circle 2")

# Centers
ax.scatter(C1[0], C1[1], color="blue", marker="x", s=100)
ax.scatter(C2[0], C2[1], color="red", marker="x", s=100)
ax.scatter(C3[0], C3[1], color="green", marker="x", s=100)

# Points (0,0) and (1,0)
ax.scatter([0, 1], [0, 0], color="black")
ax.text(0, 0, "O(0,0)", fontsize=11, ha="right", va="bottom")
ax.text(1, 0, "A(1,0)", fontsize=11, ha="left", va="bottom")

# Label centers
ax.text(C1[0], C1[1], f"C1(0,0)", fontsize=11, color="blue", ha="left", va="top")
ax.text(C2[0], C2[1], f"C2(1/2, -√2)", fontsize=11, color="red", ha="left", va="bottom")
ax.text(C3[0], C3[1], f"C3(1/2, √2)", fontsize=11, color="green", ha="left", va="bottom")

# Formatting
ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)
ax.legend(loc="upper right")

# Save figure
plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/7.4.22/figs/Figure_1.png")
plt.show()