# 🛒 E-Commerce Data Analysis (UCI Online Retail)

UCI Online Retail 데이터셋을 활용하여 이커머스 매출 및 주문 추이를 분석하고 마케팅 인사이트를 도출한 프로젝트입니다.

---

## 📈 주요 분석 내용

### 1. 월별 매출 및 주문 트렌드 분석
* `pd.to_datetime`을 활용한 시계열 데이터 전처리 및 월별 파생변수 생성
* `groupby`와 `agg(nunique)` 조합으로 월별 **총 매출액**, **주문 건수**, **객단가(AOV)** 산출
* `seaborn` 라이브러리를 활용한 매출액 추이 시계열 시각화

### 2. 시계열 데이터의 예외 사항 처리
* **2011년 12월 데이터 급감 이슈**: 데이터 분석 중 12월 매출이 폭락한 것을 발견, 확인 결과 12월 전체가 아닌 **9일치 데이터만 존재**함을 파악하여 데이터 해석의 왜곡 방지

### 3. 매출 폭증 원인 분석 (9월 트렌드)
* 2011년 9월 매출이 급증한 원인을 파악하기 위해 주문 건수와 객단가를 쪼개어 분석
* 분석 결과 주문 건수의 증가보다 **객단가(AOV)가 최고점**을 찍은 것을 확인
* **인사이트**: 대량 구매자(큰손) 유입 또는 객단가가 높은 상품의 판매 증가 가설 수립 및 검증

---

## 🛠️ 사용 기술 및 라이브러리
* **Language**: Python
* **Libraries**: Pandas, Seaborn, Matplotlib
* **Tool**: Jupyter Notebook / VS Code

---

## 📂 디렉토리 구조
```text
ecommerce/
├── data/
│   └── Online_Retail.csv       # 원본 데이터셋
├── ecommerce_analysis.ipynb    # 데이터 분석 주피터 노트북
└── README.md                   # 프로젝트 설명 문서