"""
statistics.py
Basic statistical operations
"""

import numpy as np

arr = np.array([5,10,15,20,25])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nColumn Wise Sum")
print(np.sum(matrix, axis=0))

print("\nRow Wise Sum")
print(np.sum(matrix, axis=1))