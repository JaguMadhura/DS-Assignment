import pandas as pd
#sample dataset with duplicates
df=pd.DataFrame({
    'ID':[1,2,3,4,5,5,],
    'Name':['Alice','Bob','Alice','Bob','David','Charlie'],
    'Age':[25,30,30,35,40,45]

})
print("Original Data:\n",df)
#remove exact duplicates
df_exact=df.drop_duplicates()
print("\nAfter Exact match removal:\n", df_exact)