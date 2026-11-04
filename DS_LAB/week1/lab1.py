import pandas as pd
data={'apples':[1234]}
df=pd.DataFrame(data)
print(df)

import pandas as pd
df=pd.read_csv('Iris.csv')
print(df)



df.head()

df.head(2)

df.tail()

df.tail(3)

df.info()

df.shape

import pandas as pd
df=pd.read_csv('Iris.csv')
df.shape
#hai
dup_df=pd.concat([df,df])
dup_df.shape

dup_df.drop_duplicates(inplace=True)
dup_df.shape

df.describe()

import pandas as pd
data = [1,2,3,10,20,30]
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = {'Name':['AA','BB'],'Age':[30,45]}
df = pd.DataFrame(data)
print(df)

df.to_csv('abc.csv',index=True)

data ={'col_1':[3,2,1,0],'col_2':['a','b','c','d']}
pd.DataFrame.from_dict(data)

data={'row_1':[3,2,1,0],'row_2':['a','b','c','d']}
pd.DataFrame.from_dict(data,orient='index')

data={'row_1':[3,2,1,0],'row_2':['a','b','c','d']}
pd.DataFrame.from_dict(data,orient='index')

import pandas as pd
data = {
    'Roll_No': [1,2,3,4,5,6,7,8,9,10],
    'Name': ['Alice', 'Bob', 'Usha', 'Ananya', 'Ramya','Sneha', 'Kiranmayi', 'Sindhu', 'Smitha', 'Swetha'],
    'Age': [15, 18, 17, 20, 14, 28, 20, 9, 18, 20],
    'Section': ['C', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A'],
    'Marks1': [85, 78, 92, 88, 76, 81, 95, 69, 84, 90],
    'Marks2': [80, 82, 89, 91, 74, 85, 90, 75, 88, 93],
    'Marks3': [87, 79, 94, 86, 72, 83, 96, 78, 85, 91]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("student.csv", index=True)