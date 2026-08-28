"""LOAD AND VERIFY CREDIT CARD DATASET"""

import pandas as pd
import os
print("="*50)
print("Loading Credit Card Dataset")
print("="*50)
file_path = "data/UCI_Credit_Card.csv"
if not os.path.exists(file_path):
    print("Dataset not found in data folder")
    exit()

# Load dataset of csv
df = pd.read_csv(file_path)
print(f"Records loaded: {len(df)}")
print(f"Columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())

# Identify target column
target = None
for col in df.columns:
    if "default" in col.lower():
        target = col
print(f"\nTarget column: {target}")

default_rate = df[target].mean()*100
print(f"Default rate: {default_rate:.2f}%")

# Save cleaned copy
df.to_csv("data/raw_data.csv", index=False)

print("\nDataset saved as data/raw_data.csv")
print("Data loading complete")