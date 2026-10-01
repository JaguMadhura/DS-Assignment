import pandas as pd
from scipy.stats import spearmanr

df = pd.DataFrame({
    'TOC': [23, 89, 90, 56, 56, 78],
    'CD': [90, 56, 45, 23, 12, 67],
    'MO': [90, 89, 78, 56, 45, 34]
})

c_v, p_v = spearmanr(df['TOC'], df['CD'])

print(f"Spearman correlation coefficient: {c_v}")
print(f"P-Value: {p_v}")

# Read Iris dataset
df = pd.read_csv("Iris.csv")

# Spearman correlation for all numeric columns
print(df.corr(method='spearman', numeric_only=float))