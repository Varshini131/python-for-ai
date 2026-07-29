"""
series.py
Introduction to Pandas Series
"""

import pandas as pd

# Creating a Series
numbers = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(numbers)

# Custom Index
students = pd.Series(
    [90, 85, 95],
    index=["Alice", "Bob", "Charlie"]
)

print("\nStudent Marks:")
print(students)

print("\nBob's Marks:", students["Bob"])

print("\nSeries Information")
print("Length:", len(numbers))
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())
print("Mean:", numbers.mean())
