"""
grouping.py
Grouping data
"""
import pandas as pd

data = {
    "Department": ["CSE", "ECE", "CSE", "EEE", "ECE"],
    "Marks": [90, 85, 95, 80, 88]
}
df = pd.DataFrame(data)
print(df)
print("\nAverage Marks by Department")
print(df.groupby("Department")["Marks"].mean())
print("\nMaximum Marks")
print(df.groupby("Department")["Marks"].max())