# Data Dictionary

## dim_fund

| Column        | Type    | Description                   |
| ------------- | ------- | ----------------------------- |
| amfi_code     | INTEGER | Unique AMFI scheme identifier |
| fund_house    | TEXT    | Mutual fund company           |
| scheme_name   | TEXT    | Name of the scheme            |
| category      | TEXT    | Fund category                 |
| sub_category  | TEXT    | Fund sub-category             |
| risk_category | TEXT    | Risk classification           |

## fact_nav

| Column    | Type    | Description       |
| --------- | ------- | ----------------- |
| amfi_code | INTEGER | Scheme identifier |
| date      | DATE    | NAV date          |
| nav       | REAL    | Net Asset Value   |

## fact_transactions

| Column           | Type | Description             |
| ---------------- | ---- | ----------------------- |
| investor_id      | TEXT | Investor identifier     |
| transaction_date | DATE | Date of transaction     |
| transaction_type | TEXT | SIP/Lumpsum/Redemption  |
| amount_inr       | REAL | Transaction amount      |
| kyc_status       | TEXT | KYC verification status |
