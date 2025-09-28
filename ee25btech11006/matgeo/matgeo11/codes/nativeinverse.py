import sympy as sp

A = sp.Matrix([[2, 3], [-4, -6]])
try:
    A_inv = A.inv()
    sp.pprint(A_inv)
except Exception as e:
    print("Error:", e)
    print("Matrix is singular, so no inverse exists.")