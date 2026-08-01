"""
cleaning.py
Cleaning missing data
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [21, None, 20, 23],
    "Marks": [90, 85, None, 78]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values")
print(df.isnull())

print("\nTotal Missing Values")
print(df.isnull().sum())

print("\nAfter Filling Missing Values")
filled = df.fillna(0)
print(filled)

print("\nAfter Removing Missing Values")
print(df.dropna())