import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL("./libcode.so")

# Define function signatures
lib.computeLambda.argtypes = [ctypes.c_double, ctypes.c_double]
lib.computeLambda.restype = ctypes.c_double

lib.xIntersect.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.xIntersect.restype = ctypes.c_double

lib.yIntersect.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.yIntersect.restype = ctypes.c_double

lib.zIntersect.argtypes = []
lib.zIntersect.restype = ctypes.c_double

# Given points A and B
A = np.array([3.0, 4.0, 1.0])
B = np.array([5.0, 1.0, 6.0])

# Direction vector m = B - A
m = B - A

# Compute lambda for intersection
lam = lib.computeLambda(A[2], m[2])

# Compute intersection point
X = lib.xIntersect(A[0], m[0], lam)
Y = lib.yIntersect(A[1], m[1], lam)
Z = lib.zIntersect()

intersection = np.array([X, Y, Z])
print("Intersection with XY plane:", intersection)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points A, B, intersection
ax.scatter(A[0], A[1], A[2], color='red', label='A(3,4,1)')
ax.scatter(B[0], B[1], B[2], color='blue', label='B(5,1,6)')
ax.scatter(X, Y, Z, color='green', s=100, label='Intersection XY-plane')

# Plot the line AB
line = np.vstack((A, B))
ax.plot(line[:,0], line[:,1], line[:,2], 'k--', label='Line AB')

# Plot XY-plane for reference
xx, yy = np.meshgrid(np.linspace(0, 5, 10), np.linspace(0, 5, 10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2, color='cyan')

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()