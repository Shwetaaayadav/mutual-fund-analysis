import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "="*80)
    print(f"FILE: {file}")
    print("="*80)

    file_path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")