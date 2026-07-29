"""
broadcasting.py
Broadcasting in NumPy
"""

import numpy as np

arr = np.array([1,2,3,4])

print(arr + 5)

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nMatrix + 10")
print(matrix + 10)

vector = np.array([100,200,300])

print("\nBroadcasting")
print(matrix + vector)