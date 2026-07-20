#%%     
import pandas as pd
print("⏳ 데이터를 인터넷에서 불러오는 중입니다... 잠시만 기다려주세요.")

# 온라인 쇼핑몰 데이터 로드
df = pd.read_csv("data.csv", encoding="ISO-8859-1")

print("\n" + "="*50)
print("🎉 데이터 로드 완료!")
print(f"데이터 형태 (행, 열): {df.shape}")
print("="*50)

# 터미널에 상위 5개 데이터 출력
print("\n[ 데이터 미리보기 ]")
print(df.head())

# 각 컬럼의 데이터 타입과 결측치 확인
print("\n[ 데이터 기본 정보 ]")
print(df.info())
# %%
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')  
df['InvoYearMonth'] = df['InvoiceDate'].dt.year.astype(str) + "-" + df['InvoiceDate'].dt.month.astype(str).str.zfill(2)
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

df.head()
# %%
#%% [수정된 미션 1] 정확한 월별 집계 및 시각화

# 1. 정렬하지 않은 "전체 월별 매출" 데이터프레임을 따로 만듭니다. (TotalAmount 사용!)
monthly_sales_clean = df.groupby('InvoYearMonth')['TotalAmount'].sum().reset_index()

# 2. 터미널/대화형 창 확인용 상위 10개는 출력할 때만 정렬해서 보기
print("\n[ 월별 총 매출 상위 10개 (실제 매출액 기준) ]")
print(monthly_sales_clean.sort_values(by='TotalAmount', ascending=False))

# 3. 그래프 그리기 (데이터 소스를 새로 만든 monthly_sales_clean으로 지정!)
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
# x축은 연월, y축은 진짜 총매출액(TotalAmount)
sns.lineplot(data=monthly_sales_clean, x='InvoYearMonth', y='TotalAmount', marker='o', color='b')

plt.title('Monthly Total Sales Trajectory')
plt.xticks(rotation=45) # 글자가 겹치지 않게 회전
plt.grid(True)
plt.show()
# %%
monthly_orders_clean = df.groupby('InvoYearMonth')['Quantity'].nunique().reset_index()
print("\n[ 월별 총 주문 수 상위 10개 (실제 주문 수 기준) ]")
print(monthly_orders_clean.sort_values(by='Quantity', ascending=False))
# %%
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_orders_clean, x='InvoYearMonth', y='Quantity', marker='o', color='g')

plt.title('Monthly Total Orders Trajectory')
plt.xticks(rotation=45) # 글자가 겹치지 않게 회전
plt.grid(True)
plt.show()
# %%
monthly_aov = df.groupby('InvoYearMonth').agg({'TotalAmount':'sum', 'InvoiceNo':'nunique'}).reset_index()
monthly_aov ['AverageOrderValue']= monthly_aov['TotalAmount'] / monthly_aov['InvoiceNo']
print("\n[ 월별 평균 주문 금액 (AOV)]")
print(monthly_aov)

sns.lineplot(data=monthly_aov, x='InvoYearMonth', y='AverageOrderValue', marker='o', color='r')
plt.title('Monthly Average Order Value (AOV) Trajectory')   
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
# %%
