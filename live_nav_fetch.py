import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, code in schemes.items():

    print(f"\nFetching {scheme_name}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = f"data/raw/live_nav/{scheme_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    else:
        print(f"Failed for {scheme_name}")