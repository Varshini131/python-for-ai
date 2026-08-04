"""
preprocessing.py
Data preprocessing using Scikit-learn
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [18, 20, 22, 24, 26],
    "Salary": [20000, 25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

scaler = StandardScaler()

scaled = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled, columns=df.columns)

print("\nScaled Data")
print(scaled_df)