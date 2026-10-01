import pandas as pd

df = pd.DataFrame({
    'TOC':[23,89,90,56,56,78],
    'CD':[90,56,45,23,12,67],
    'MO':[90,89,78,56,45,34]})

c_m = df.corr(method='pearson')
print("Pearson correlation matrix:\n",c_m)

df = pd.read_csv("Iris.csv")
print(df.corr(method='pearson',numeric_only=float))