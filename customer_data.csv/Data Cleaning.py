import pandas as pd
df = pd.read_csv("customer_data.csv")

print(df.isnull().sum())

df.fillna({'age': df['age'].mean}, inplace=True)

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.dtypes)

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'].fillna(df['age'].mean(), inplace=True)
df['age'] = df['age'].astype(int)
print(df.dtypes)


df.to_csv('customer_data.csv', index=False)