import pandas as pd
import os

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_path, file))

        print("\n" + "="*50)
        print(file)
        print(df.shape)
        print(df.dtypes)
        print(df.head())