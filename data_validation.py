import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")


print("\nFund Master Shape:")
print(fund_master.shape)

print("\nColumns:")
print(fund_master.columns.tolist())


print("\nUnique Fund Houses:")

for house in sorted(fund_master["fund_house"].dropna().unique()):
    print(house)


print("\nUnique Categories:")

for category in sorted(fund_master["category"].dropna().unique()):
    print(category)


print("\nUnique Sub Categories:")

for subcat in sorted(fund_master["sub_category"].dropna().unique()):
    print(subcat)


print("\nUnique Risk Categories:")

for risk in sorted(fund_master["risk_category"].dropna().unique()):
    print(risk)


print("\nAMFI Validation")

master_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

missing_codes = master_codes - nav_codes

print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")
print(f"Missing Codes     : {len(missing_codes)}")

if len(missing_codes) > 0:

    print("\nMissing AMFI Codes:")

    for code in sorted(missing_codes):
        print(code)

else:

    print("\nAll AMFI Codes Successfully Validated")

coverage = (
    len(master_codes.intersection(nav_codes))
    / len(master_codes)
) * 100

print(f"\nCoverage Percentage: {coverage:.2f}%")


print("\nMissing Values in Fund Master:")
print(fund_master.isnull().sum())

print("\nMissing Values in NAV History:")
print(nav_history.isnull().sum())


print("\nDuplicate Records")

print(
    f"Fund Master : {fund_master.duplicated().sum()}"
)

print(
    f"NAV History : {nav_history.duplicated().sum()}"
)