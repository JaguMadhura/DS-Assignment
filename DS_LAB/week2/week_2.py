import pandas as pd
import numpy as np

# Sample dataset
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})

print("Original DataFrame:")
print(df)

# Fill missing numeric values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing categorical values with mode
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])


print(df)