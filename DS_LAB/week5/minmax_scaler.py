import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
    'A':[10,20,30,40,78],
    'B':[5,34,56,89,70]
})
print(data)

scaler = MinMaxScaler()
normalized_dta = scaler.fit_transform(data)

normalized_df = pd.DataFrame(normalized_dta, columns=data.columns)
print("Normalized data (min-Max scaling):")
print(normalized_df)