"""
reading_csv.py
Reading CSV files
"""

import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 20],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("students.csv", index=False)

print("CSV file created.")

# Read CSV
students = pd.read_csv("students.csv")

print("\nCSV Data")
print(students)