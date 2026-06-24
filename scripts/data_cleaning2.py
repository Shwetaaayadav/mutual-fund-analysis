import pandas as pd

datasets = [
    ("01_fund_master.csv",
     "01_fund_master_clean.csv"),

    ("03_aum_by_fund_house.csv",
     "03_aum_by_fund_house_clean.csv"),

    ("04_monthly_sip_inflows.csv",
     "04_monthly_sip_inflows_clean.csv"),

    ("05_category_inflows.csv",
     "05_category_inflows_clean.csv"),

    ("06_industry_folio_count.csv",
     "06_industry_folio_count_clean.csv"),

    ("09_portfolio_holdings.csv",
     "09_portfolio_holdings_clean.csv"),

    ("10_benchmark_indices.csv",
     "10_benchmark_indices_clean.csv")
]

for raw_file, clean_file in datasets:

    df = pd.read_csv(
        f"data/raw/{raw_file}"
    )

    df = df.drop_duplicates()

    df.to_csv(
        f"data/processed/{clean_file}",
        index=False
    )

    print(
        f"Saved {clean_file}"
    )