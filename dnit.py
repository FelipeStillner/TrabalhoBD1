import pandas as pd
import numpy as np

df = pd.read_csv("initialCsv/dnitmarco2024.csv", on_bad_lines='skip')

section = df[['UF', "Rodovia", "km inicial", "Data", "Latitude", "Longitude", "IC", "IP", "ICM"]]

section.rename(columns={"UF": "stateid", "Rodovia": "code", "km inicial": "km"}, inplace=True)

section.dropna(inplace=True)

for index, row in section.iterrows():
    row["code"] = (row["code"])[3:]
    try:
        row["km"] = float(row["km"]).__floor__()
    except:
        row["code"] = np.nan
        
section.dropna(inplace=True)

section.drop_duplicates(subset=['km', 'code'], inplace=True)

section.sort_values(by=['code', 'km'])

section.to_csv("partialCsv/section.csv", index=False)
