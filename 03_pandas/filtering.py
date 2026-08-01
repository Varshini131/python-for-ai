"""
filtering.py
Filtering data in Pandas
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 22, 20, 23],
    "Marks": [90, 85, 95, 78]
}

df = pd.DataFrame(data)

print(df)

print("\nStudents scoring above 85")
print(df[df["Marks"] > 85])

print("\nStudents older than 21")
print(df[df["Age"] > 21])

print("\nSelected Columns")
print(df[["Name", "Marks"]])