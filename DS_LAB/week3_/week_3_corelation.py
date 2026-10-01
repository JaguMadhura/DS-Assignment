import pandas as pd

df = pd.DataFrame({
    'X':[10,20,30,40,50,60],
    'Y':[12,45,90,45,12,34]
})
c_m = df.corr(method='pearson')
print("Pearson correlation matrix:\n",c_m)
