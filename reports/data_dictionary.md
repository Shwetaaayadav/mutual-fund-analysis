# Data Dictionary

## 01_fund_master.csv

| Column            | Data Type |Description                     |
| ----------------- | --------- | ------------------------------- |
| amfi_code         | Integer   | Unique AMFI scheme identifier   |
| fund_house        | Text      | Mutual fund company name        |
| scheme_name       | Text      | Scheme name                     |
| category          | Text      | Fund category                   |
| sub_category      | Text      | Detailed category               |
| expense_ratio_pct | Float     | Annual expense ratio percentage |

## 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

## 03_aum_by_fund_house.csv

| Column     | Data Type | Description             |
| ---------- | --------- | ----------------------- |
| date       | Date      | Reporting date          |
| fund_house | Text      | AMC name                |
| aum_crore  | Float     | Assets Under Management |

## 07_scheme_performance.csv

| Column            | Data Type | Description                 |
| ----------------- | --------- | --------------------------- |
| return_1yr_pct    | Float     | 1-year return               |
| return_3yr_pct    | Float     | 3-year return               |
| return_5yr_pct    | Float     | 5-year return               |
| sharpe_ratio      | Float     | Risk-adjusted return metric |
| expense_ratio_pct | Float     | Expense ratio               |

## 08_investor_transactions.csv

| Column           | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| investor_id      | Integer   | Unique investor ID      |
| transaction_date | Date      | Transaction date        |
| amount_inr       | Float     | Transaction amount      |
| transaction_type | Text      | SIP/Lumpsum/Redemption  |
| kyc_status       | Text      | KYC verification status |
