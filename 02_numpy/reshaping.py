"""
reshaping.py
Changing array shape
"""

import numpy as np

arr = np.arange(1,13)

print("Original")
print(arr)

matrix = arr.reshape(3,4)

print("\nReshaped")
print(matrix)

print("\nFlatten")
print(matrix.flatten())

print("\nTranspose")
print(matrix.T)