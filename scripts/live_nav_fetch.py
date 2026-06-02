import requests
import pandas as pd
import os


# Mutual Fund Schemes
schemes = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

for scheme_name, scheme_code in schemes.items():
    try:
        print(f"Fetching {scheme_name}...")

        url = f"https://api.mfapi.in/mf/{scheme_code}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # NAV history
        nav_df = pd.DataFrame(data["data"])

        # Save CSV
        file_path = f"data/raw/{scheme_name}.csv"
        nav_df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")
        print(f"Rows: {nav_df.shape[0]}, Columns: {nav_df.shape[1]}\n")

    except Exception as e:
        print(f"Error fetching {scheme_name}: {e}")

print("All NAV data downloaded successfully!")