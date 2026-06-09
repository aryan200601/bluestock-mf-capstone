# import pandas as pd

# performance = pd.read_csv(
#     "data/processd/clean_performance.csv"
# )

# def recommend_funds(risk_appetite):

#     filtered = performance[
#         performance['risk_grade'] == risk_appetite
#     ]

#     top3 = (
#         filtered
#         .sort_values(
#             'sharpe_ratio',
#             ascending=False
#         )
#         .head(3)
#     )

#     return top3[
#         [
#             'scheme_name',
#             'sharpe_ratio',
#             'risk_grade'
#         ]
#     ]

# print(recommend_funds("Moderate"))







# Sector Concentration Analysis (HHI)
# Objective


# Where:

# weight_i = sector weight percentage

# Higher HHI = More concentrated portfolio

# Lower HHI = Better diversified portfolio




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load holdings data
holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

# Aggregate sector weights per fund
sector_weights = (
    holdings
    .groupby(['amfi_code', 'sector'])['weight_pct']
    .sum()
    .reset_index()
)

# Calculate HHI
sector_weights['weight_sq'] = (
    sector_weights['weight_pct'] / 100
) ** 2

sector_hhi = (
    sector_weights
    .groupby('amfi_code')['weight_sq']
    .sum()
    .reset_index()
)

sector_hhi.rename(
    columns={'weight_sq': 'HHI'},
    inplace=True
)

# Sort descending
sector_hhi = sector_hhi.sort_values(
    'HHI',
    ascending=False
)

print(sector_hhi.head(10))

# Save CSV
sector_hhi.to_csv(
    "reports/sector_hhi.csv",
    index=False
)

# Chart
top10 = sector_hhi.head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top10['amfi_code'].astype(str),
    top10['HHI']
)

plt.title(
    "Top 10 Most Concentrated Funds (HHI)"
)

plt.xlabel("Fund")
plt.ylabel("HHI")

plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()

plt.savefig(
    "reports/charts/sector_hhi_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Task 6 Completed")