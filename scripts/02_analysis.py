"""
CREDIT CARD DATA ANALYSIS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

print("="*50)
print("Credit Card Default Analysis")
print("="*50)

# Load dataset
df = pd.read_csv("data/raw_data.csv")

# Identify target column
target = None
for col in df.columns:
    if "default" in col.lower():
        target = col

print(f"Target variable: {target}")

# Basic statistics
print("\nDataset Statistics")
print("--------------------")

print(f"Total customers: {len(df)}")
print(f"Default rate: {df[target].mean()*100:.2f}%")
print(f"Average credit limit: {df['LIMIT_BAL'].mean():,.0f}")
print(f"Average age: {df['AGE'].mean():.2f}")

# Create output folder
os.makedirs("output/figures", exist_ok=True)

# Default distribution
plt.figure(figsize=(6,4))
df[target].value_counts().plot(kind="bar")
plt.title("Default Distribution")
plt.xlabel("Default (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.savefig("output/figures/default_distribution.png")
plt.close()

# Credit limit vs default
plt.figure(figsize=(8,5))
sns.boxplot(x=df[target], y=df["LIMIT_BAL"])
plt.title("Credit Limit vs Default")
plt.savefig("output/figures/credit_limit_vs_default.png")
plt.close()

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df["AGE"], bins=30)
plt.title("Age Distribution")
plt.savefig("output/figures/age_distribution.png")
plt.close()

print("Charts saved to output/figures")

# Statistical test
print("\nRunning T-Test: Credit Limit")

group0 = df[df[target]==0]["LIMIT_BAL"]
group1 = df[df[target]==1]["LIMIT_BAL"]

t_stat, p_val = stats.ttest_ind(group0, group1)

print(f"T statistic: {t_stat:.4f}")
print(f"P value: {p_val:.6f}")

if p_val < 0.05:
    print("Result: Significant difference between groups")
else:
    print("Result: No significant difference")


# CLEAN HEATMAP 


print("\n📊 Creating PROFESSIONAL heatmap...")

import seaborn as sns

# Select numeric data
numeric_df = df.select_dtypes(include=['number'])

# Correlation matrix
corr = numeric_df.corr()

# Focus on target variable
target_corr = corr[target].abs().sort_values(ascending=False)

# Select top important features (excluding target itself)
top_features = target_corr[1:9].index

# Reduced correlation matrix
reduced_corr = numeric_df[top_features].corr()

# Plot heatmap
plt.figure(figsize=(10,8))

sns.heatmap(
    reduced_corr,
    annot=True,              # show values
    fmt=".2f",               # 2 decimal places
    cmap="coolwarm",         # professional color
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.8}
)

plt.title("Key Feature Correlation Heatmap", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()

# Save image
plt.savefig('output/figures/correlation_heatmap.png', dpi=300)
plt.close()

print("✅ Saved: output/figures/correlation_heatmap.png")

print("\nAnalysis complete")