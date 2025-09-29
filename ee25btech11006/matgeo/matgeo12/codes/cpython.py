import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared C library
rect_lib = ctypes.CDLL('./rect.so')

# Define the C function signature
calculate_dimensions_c = rect_lib.calculate_dimensions
calculate_dimensions_c.argtypes = [
    ctypes.c_float, ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)
]
calculate_dimensions_c.restype = None

# Inputs
perimeter = 36.0
difference = 4.0

# Output variables
length = ctypes.c_float()
breadth = ctypes.c_float()

# Call the C function
calculate_dimensions_c(perimeter, difference, ctypes.byref(length), ctypes.byref(breadth))

# Extract values
L = length.value
B = breadth.value

print("--- Rectangle Dimensions from C function ---")
print(f"Length: {L:.2f} units")
print(f"Breadth: {B:.2f} units")
print("--------------------------------------------")

# Define rectangle corners
A = np.array([0, 0])
B_pt = np.array([L, 0])
C = np.array([L, B])
D = np.array([0, B])
rectangle = np.array([A, B_pt, C, D, A])

# Plot
fig, ax = plt.subplots()
ax.plot(rectangle[:, 0], rectangle[:, 1], 'b-', marker='o', markersize=8)

# Labels
labels = {'A': A, 'B': B_pt, 'C': C, 'D': D}
for label, pt in labels.items():
    ax.text(pt[0], pt[1] + 0.3, label, fontsize=14, ha='center')

# Dimension annotations
ax.text(L / 2, -0.8, f'Length = {L:.2f}', fontsize=12, ha='center')
ax.text(L + 0.8, B / 2, f'Breadth = {B:.2f}', fontsize=12, va='center', rotation=90)

# Right angle markers
def draw_right_angle(x, y, size=0.5):
    ax.plot([x, x + size], [y, y], 'r-', linewidth=1)
    ax.plot([x, x], [y, y + size], 'r-', linewidth=1)

draw_right_angle(*A)
draw_right_angle(*B_pt)
draw_right_angle(*C)
draw_right_angle(*D)

# Finalize plot
ax.set_aspect('equal')
ax.axis('off')
plt.title('Rectangle from C-calculated Dimensions', fontsize=14)
plt.savefig('../figs/rectangle.png')
plt.show()