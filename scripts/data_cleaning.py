import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)


nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)


txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .replace({
        "Sip": "SIP",
        "Lumpsum": "Lumpsum",
        "Redemption": "Redemption"
    })
)

invalid_amount = txn[
    txn["amount_inr"] <= 0
]

print(
    "Invalid Amount Records:",
    len(invalid_amount)
)

print(
    "KYC Values:",
    txn["kyc_status"].unique()
)

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)


perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["return_1yr_pct"] > 100)
    |
    (perf["return_1yr_pct"] < -100)
]

print(
    "Return Anomalies:",
    len(anomalies)
)

expense_issues = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    "Expense Ratio Issues:",
    len(expense_issues)
)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nCleaning Completed Successfully")