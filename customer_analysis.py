#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', encoding='ISO-8859-1')
df.head()
# %%
df_cleaned = df.dropna(subset=['CustomerID'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
total_spent = df.groupby('CustomerID')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)  
total_purchases = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index().sort_values(by='InvoiceNo', ascending=False)    

print(total_spent.head())
print(total_purchases.head())
# %%
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df_cleaned = df.dropna(subset=['CustomerID'])

customer_summary = df_cleaned.groupby('CustomerID').agg(
    total_spent=('TotalPrice', 'sum'),
    total_purchases=('InvoiceNo', 'nunique')
).reset_index()

customer_summary = customer_summary.sort_values(by='total_spent', ascending=False)
print(customer_summary.head())
# %%
customer_summary = pd.merge(total_spent, total_purchases, on='CustomerID')
customer_summary.columns = ['CustomerID', 'TotalSpent', 'order_count']

# %%
print(customer_summary.head())
# %%
total_customers = len(customer_summary)
top_1_customers = total_customers * 0.01
total_spent_top_customers = customer_summary.head(int(top_1_customers))['TotalSpent'].sum()
total_spent_all_customers = customer_summary['TotalSpent'].sum()
top_1_contribution = (total_spent_top_customers / total_spent_all_customers) * 100
print(f"총 고객 수: {total_customers}")
print(f"상위 1% 고객 수: {int(top_1_customers)}")
print(f"상위 1% 고객의 총 매출 기여도: {top_1_contribution:.2f}%")

# %%
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')  
df['InvoYearMonth'] = df['InvoiceDate'].dt.year.astype(str) + "-" + df['InvoiceDate'].dt.month.astype(str).str.zfill(2)
# %%
sep_df = df[df['InvoYearMonth'] == '2011-09']
set_top_customers = sep_df.groupby('CustomerID').agg(
    total_spent=('TotalPrice', 'sum'),
    total_purchases=('InvoiceNo', 'nunique')
).reset_index()

sep_df_top_customers = set_top_customers.sort_values(by='total_spent', ascending=False)
print(sep_df_top_customers.head(10))

# %%
