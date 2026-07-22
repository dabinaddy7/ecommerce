#%%
import pandas as pd

df = pd.read_csv('data.csv', encoding='ISO-8859-1')
df_cleaned = df.dropna(subset=['CustomerID'])
print(df_cleaned[df_cleaned['CustomerID'] == 17450])

# %%
df_cleaned['TotalPrice'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']
vip_df = df_cleaned[df_cleaned['CustomerID'] == 17450]  
vip_products = vip_df.groupby('Description')[['Quantity', 'TotalPrice']].sum()
vip_products_sorted= vip_products.sort_values(by='TotalPrice', ascending=False)
print(vip_products_sorted)

# %%
top_products = df_cleaned.groupby('Description')[['Quantity', 'TotalPrice']].sum()
top_products_sorted = top_products.sort_values(by='TotalPrice', ascending=False)
print(top_products_sorted.head(10))
# %%
top_products_sorted_by_quantity = top_products.sort_values(by='Quantity', ascending=False)
print(top_products_sorted_by_quantity.head(10))
# %%
