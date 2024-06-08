import pandas as pd
import numpy as np

df = pd.read_csv("initialCsv/municipios.csv", encoding='latin-1', on_bad_lines='skip', sep=";")

cities = df[['CÓDIGO DO MUNICÍPIO - IBGE', "MUNICÍPIO - IBGE", "UF"]]

cities.rename(columns={"CÓDIGO DO MUNICÍPIO - IBGE": "cityid", "MUNICÍPIO - IBGE": "name", "UF": "stateid"}, inplace=True)

cities.drop_duplicates("name", inplace=True)

cities.replace("EX", np.nan, inplace=True)

cities.dropna(inplace=True)

cities.to_csv("finalCsv/city.csv", index=False, header=False)
