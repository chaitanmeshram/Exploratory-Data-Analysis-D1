import pandas as pd
df = pd.read_csv("sales_data.csv")

print(df.isnull().sum())

print(df.duplicated().sum())

df['invoice_date'].fillna(df['invoice_date'].mode()[0], inplace=True)

print(df.isnull().sum())

print(df.dtypes)
df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
print(df.dtypes)
df.to_csv("sales_data.csv", index=False)