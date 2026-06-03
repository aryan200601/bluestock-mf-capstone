-- -- Top 5 funds by AUM
-- SELECT *
-- FROM fact_aum
-- ORDER BY aum DESC
-- LIMIT 5;


-- SELECT
-- state,
-- COUNT(*) AS total_transactions
-- FROM fact_transactions
-- GROUP BY state
-- ORDER BY total_transactions DESC;
-- SELECT
-- state,
-- COUNT(*) AS total_transactions
-- FROM fact_transactions
-- GROUP BY state
-- ORDER BY total_transactions DESC;
-- SELECT
-- transaction_type,
-- SUM(amount_inr) AS total_amount
-- FROM fact_transactions
-- GROUP BY transaction_type;
-- SELECT
-- scheme_name,
-- expense_ratio_pct
-- FROM dim_fund
-- WHERE expense_ratio_pct < 1;
-- SELECT
-- category,
-- COUNT(*) AS fund_count
-- FROM dim_fund
-- GROUP BY category;
-- SELECT
-- risk_category,
-- COUNT(*) AS fund_count
-- FROM dim_fund
-- GROUP BY risk_category;
-- SELECT
-- category,
-- AVG(expense_ratio_pct) AS avg_expense_ratio
-- FROM dim_fund
-- GROUP BY category;
SELECT
kyc_status,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;