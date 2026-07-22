#%%
import pandas as pd
df = pd.read_csv('data.csv', encoding='ISO-8859-1')
df_cleaned = df.dropna(subset='CustomerID')
df_cleaned['TotalPrice'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']
# %%
non_products = ['POSTAGE', 'Manual', 'Discount', 'CRUK Commission', 'DOTCOM POSTAGE']

cond1 = df_cleaned['Quantity'] >0
cond2 = df_cleaned['UnitPrice'] >0
cond3= ~df_cleaned['Description'].isin(non_products)

df_pure = df_cleaned[cond1 & cond2 & cond3]
                   
# %%
# 데이터 건수 비교
print(f"정제 전 데이터 건수: {len(df_cleaned)}")
print(f"정제 후 데이터 건수: {len(df_pure)}")

# 총 매출액 비교
print(f"정제 전 총 매출: {df_cleaned['TotalPrice'].sum():,.2f}")
print(f"정제 후 총 매출: {df_pure['TotalPrice'].sum():,.2f}")
# %%
pure_top_products = df_pure.groupby('Description')[['Quantity', 'TotalPrice']].sum()
print(pure_top_products.sort_values(by = 'TotalPrice', ascending=False).head())
# %%
df_pure['InvoiceDate'] = pd.to_datetime(df_pure['InvoiceDate'])
df_pure['InvoiceDate']
# %%
year_and_month = df_pure['InvoiceDate'].dt.to_period('M')
day = df_pure['InvoiceDate'].dt.day_name()
hour = df_pure['InvoiceDate'].dt.hour

print(year_and_month)
print(day)
print(hour)
# %%
year_and_month_summary = df_pure.groupby(year_and_month)['TotalPrice'].sum().sort_values(ascending=False)
day_summary = df_pure.groupby(day)['TotalPrice'].sum().sort_values(ascending=False)
hour_summary = df_pure.groupby(hour)['TotalPrice'].sum().sort_values(ascending=False)

print(year_and_month_summary.head(10))
print('='*50)
print(day_summary.head(10))
print('='*50)
print(hour_summary.head(10))


# %%
