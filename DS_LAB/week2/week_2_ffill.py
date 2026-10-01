import pandas as pd
import numpy as np

df = pd.DataFrame ({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
print(df)
print("\nDataFrame after filling missing values:")
print("\n")

df_dup = df.copy()
df_dup.ffill(inplace = True)
print(df_dup)
#backfill
df_bfill = df.copy()
df_bfill.bfill(inplace=True)

print("DataFrame after bfill():")
print(df_bfill)