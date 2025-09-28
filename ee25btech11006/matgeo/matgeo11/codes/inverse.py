import ctypes
import numpy as np
import sympy as sp

lib = ctypes.CDLL("./libinverse.so")
lib.inverse.argtypes = [ctypes.POINTER((ctypes.c_double * 2) * 2),
                        ctypes.POINTER((ctypes.c_double * 2) * 2)]
lib.inverse.restype = ctypes.c_int

A = np.array([[2, 3],
              [-4, -6]], dtype=np.double)

inv = np.zeros((2,2), dtype=np.double)

status = lib.inverse(A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)),
                     inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)))

if status == 0:
    inverse=sp.Matrix(inv)
    sp.pprint(inverse)
else:
    print("Matrix is singular, no inverse.")