from sqlalchemy import create_engine
import pandas as pd
import os

os.makedirs("database", exist_ok=True)

engine = create_engine(
    "sqlite:///database/mutual_funds.db"
)


fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)


fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)


tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\nRow Counts")

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    )

    print(
        table,
        ":",
        count.iloc[0]["cnt"]
    )