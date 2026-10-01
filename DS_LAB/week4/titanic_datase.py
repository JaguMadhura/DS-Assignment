import seaborn as sns
import pandas as pd

df = sns.load_dataset("student")

# Fill missing age values with median
df['age'] = df['age'].fillna(df['age'].median())

# Fill missing embarked values with mode
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert categorical columns into dummy variables
df = pd.get_dummies(
    df,
    columns=['sex', 'class', 'embarked'],
    drop_first=True
)

# Create family size
df['family_size'] = df['sibsp'] + df['parch']

print(df.head())