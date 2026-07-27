"""
arrays.py
Creating NumPy arrays
"""

import numpy as np

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr1)

# 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

# Array Properties
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("Size:", arr2.size)

# Special Arrays
print("\nZeros")
print(np.zeros((2, 3)))

print("\nOnes")
print(np.ones((3, 2)))

print("\nIdentity Matrix")
print(np.eye(3))

print("\nRange")
print(np.arange(1, 11, 2))

print("\nEvenly Spaced Numbers")
print(np.linspace(0, 1, 5))