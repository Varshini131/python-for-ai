"""
indexing.py
Accessing array elements
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nElement:", matrix[1, 2])
print("First Row:", matrix[0])
print("Second Column:", matrix[:, 1])