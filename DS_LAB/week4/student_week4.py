import pandas as pd

df = pd.read_csv("student.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])

df.drop_duplicates(inplace=True)

df = pd.get_dummies(df, columns=['Gender', 'Department', 'City'], drop_first=True)

print(df.head())
print(df.shape)