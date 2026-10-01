import pandas as pd
#sample dataset with duplicates
df=pd.DataFrame({
    'ID':[1,2,3,4,5,5,],
    'Name':['Alice','Bob','Alice','Bob','David','Charlie'],
    'Age':[25,30,30,35,40,45]

})
print("Original Data:\n",df)
df_subset_id=df.drop_duplicates(subset=['ID'])
print("\nAfter subset-based removal (ID):\n",df_subset_id)
df_subset_name=df.drop_duplicates(subset=['Name'])
print("\nAfter subset-based removal (Name):\n", df_subset_name)