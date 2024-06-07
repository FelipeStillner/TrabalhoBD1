import pandas as pd

df = pd.read_csv("initialCsv/municipios.csv", encoding='latin-1', on_bad_lines='skip', sep=";")

cities = df[['CÓDIGO DO MUNICÍPIO - IBGE', "MUNICÍPIO - IBGE", "UF"]]

cities.rename(columns={"CÓDIGO DO MUNICÍPIO - IBGE": "cityid", "MUNICÍPIO - IBGE": "name", "UF": "stateid"}, inplace=True)

cities.to_csv("finalCsv/cities.csv", index=False)
