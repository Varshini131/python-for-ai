"""
dataframe.py
Creating and working with DataFrames
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 20],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(data)

print("DataFrame")
print(df)

print("\nColumns")
print(df.columns)

print("\nShape")
print(df.shape)

print("\nFirst Two Rows")
print(df.head(2))

print("\nLast Row")
print(df.tail(1))