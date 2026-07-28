"""
slicing.py
Slicing NumPy arrays
"""

import numpy as np

arr = np.array([10,20,30,40,50,60,70])

print(arr[1:5])
print(arr[:4])
print(arr[3:])
print(arr[::2])
print(arr[::-1])

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\nRows 1-2")
print(matrix[0:2])

print("\nColumns 2-3")
print(matrix[:,1:3])

print("\nSub Matrix")
print(matrix[0:2,1:3])