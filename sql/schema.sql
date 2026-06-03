-- CREATE TABLE dim_fund (
--     amfi_code INTEGER PRIMARY KEY,
--     fund_house TEXT,
--     scheme_name TEXT,
--     category TEXT,
--     sub_category TEXT,
--     plan TEXT,
--     launch_date DATE,
--     benchmark TEXT,
--     expense_ratio_pct REAL,
--     exit_load_pct REAL,
--     fund_manager TEXT,
--     risk_category TEXT
-- );

-- CREATE TABLE dim_date (
--     date_id INTEGER PRIMARY KEY,
--     full_date DATE,
--     year INTEGER,
--     month INTEGER,
--     quarter INTEGER
-- );

-- CREATE TABLE fact_nav (
--     amfi_code INTEGER,
--     nav_date DATE,
--     nav REAL,
--     FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
-- );

-- CREATE TABLE fact_transactions (
--     investor_id TEXT,
--     amfi_code INTEGER,
--     transaction_date DATE,
--     transaction_type TEXT,
--     amount_inr REAL,
--     state TEXT,
--     kyc_status TEXT,
--     FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
-- );

-- CREATE TABLE fact_performance (
--     amfi_code INTEGER,
--     return_1y REAL,
--     return_3y REAL,
--     return_5y REAL,
--     sharpe_ratio REAL,
--     expense_ratio REAL,
--     FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
-- );

-- CREATE TABLE fact_aum (
--     amfi_code INTEGER,
--     aum REAL,
--     report_date DATE,
--     FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
-- );
-- SELECT name
-- FROM sqlite_master
-- WHERE type='table';
import pandas as pd

fund_master = pd.read_csv("../data/processed/clean_fund_master.csv")

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)