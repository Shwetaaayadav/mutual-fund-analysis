-- Top 5 Funds by AUM
SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

--Average NAV Per Month
SELECT
substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

--Transactions by State
SELECT
state,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

--Funds with Expense Ratio < 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

--Average Return by Fund House
SELECT
fund_house,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return DESC;

--Top Sharpe Ratio Funds
SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

--Highest NAV Scheme
SELECT
amfi_code,
MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC;

--Transaction Type Distribution
SELECT
transaction_type,
COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;

--Average AUM by Fund House
SELECT
fund_house,
AVG(aum_crore) AS avg_aum
FROM fact_aum
GROUP BY fund_house;

--Top Performing Fund
SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 1;