import pandas as pd
import numpy as np

df = pd.read_csv("initialCsv/dnitmarco2024.csv")

print(df.head())

section = df.copy()

section.rename(columns={"UF": "stateid", "Rodovia": "code", "km inicial": "km"}, inplace=True)

newsection = section[['stateid', "code", "km", "Data", "Latitude", "Longitude", "IC", "IP", "ICM"]].copy()

print(df.head())
print(newsection.head())

for index, row in section.iterrows():
    if (row[5] == "X"):
        newsection.at[index, "panela"] = 'A'
    elif (row[6] == "X"):
        newsection.at[index, "panela"] = 'M'
    else:
        newsection.at[index, "panela"] = 'B'
    if (row[8] == "X"):
        newsection.at[index, "remendo"] = 'A'
    elif (row[9] == "X"):
        newsection.at[index, "remendo"] = 'M'
    else:
        newsection.at[index, "remendo"] = 'B'
    if (row[11] == "X"):
        newsection.at[index, "trincamento"] = 'A'
    elif (row[12] == "X"):
        newsection.at[index, "trincamento"] = 'M'
    else:
        newsection.at[index, "trincamento"] = 'B'
        
    if (row[14] == "X"):
        newsection.at[index, "rocada"] = 'A'
    elif (row[15] == "X"):
        newsection.at[index, "rocada"] = 'M'
    else:
        newsection.at[index, "rocada"] = 'B'
    if (row[17] == "X"):
        newsection.at[index, "drenagem"] = 'A'
    elif (row[18] == "X"):
        newsection.at[index, "drenagem"] = 'M'
    else:
        newsection.at[index, "drenagem"] = 'B'
    if (row[20] == "X"):
        newsection.at[index, "sinalizacao"] = 'A'
    elif (row[21] == "X"):
        newsection.at[index, "sinalizacao"] = 'M'
    else:
        newsection.at[index, "sinalizacao"] = 'B'
        
    
    newsection.at[index, "code"] = (str(row["code"]))[3:]
    try:
        newsection.at[index, "km"] = float(row["km"]).__floor__()
    except:
        newsection.at[index, "code"] = np.nan
newsection.dropna(inplace=True)

newsection.drop_duplicates(subset=['km', 'code'], inplace=True)

newsection.sort_values(by=['code', 'km'])

print(newsection.head())

newsection.to_csv("partialCsv/section.csv", index=False)
