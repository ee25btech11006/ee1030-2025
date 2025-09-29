import numpy as np
import matplotlib.pyplot as plt

# Rectangle dimensions
length = 11
width = 4

# Define rectangle corners using NumPy arrays
A = np.array([0, 0])
B = np.array([length, 0])
C = np.array([length, width])
D = np.array([0, width])

# Create a list of points to draw the rectangle
rectangle = np.array([A, B, C, D, A])  # Loop back to A to close the shape

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-', linewidth=2)  # Rectangle outline

# Mark and label corners
corners = {'A': A, 'B': B, 'C': C, 'D': D}
for label, point in corners.items():
    plt.plot(point[0], point[1], 'ro')  # Red dot at corner
    plt.text(point[0], point[1] + 0.3, label, fontsize=12, ha='center')

# Add dimension labels
plt.text(length / 2, -0.8, f'Length = {length}', fontsize=12, ha='center')
plt.text(length + 0.8, width / 2, f'Width = {width}', fontsize=12, va='center', rotation=90)

# Formatting
plt.axis('equal')
plt.axis('off')
plt.title('Rectangle with Labeled Dimensions', fontsize=14)
plt.show()