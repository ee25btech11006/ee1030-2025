import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
vec1 = np.array([3, -6, 1])
lambda_val = 2/3
vec2 = np.array([2, -4, lambda_val])

# Plotting as lines from origin
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# For better visibility, create arrays for line plotting
ax.plot([0, vec1[0]], [0, vec1[1]], [0, vec1[2]], color='blue', linewidth=2, label='3i-6j+k')
ax.plot([0, vec2[0]], [0, vec2[1]], [0, vec2[2]], color='green', linewidth=2, label=f'2i-4j+λk, λ={lambda_val:.2f}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Parallel Vectors in 3D')
ax.legend()
ax.set_box_aspect([1,1,1])  # make aspect ratio equal
plt.show()