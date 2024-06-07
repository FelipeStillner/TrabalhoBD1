import pandas as pd

df = pd.read_csv("initialCsv/prf2023agrpesstodas.csv", encoding='latin-1', on_bad_lines='skip', sep=";")

crash = df[["id", "data_inversa", "horario", "br", "km", "causa_principal", "causa_acidente", "ordem_tipo_acidente", "tipo_acidente", "classificacao_acidente", "fase_dia", "sentido_via", "condicao_metereologica", "tipo_pista", "tracado_via", "uso_solo", "ilesos", "feridos_leves", "feridos_graves", "mortos", "latitude", "longitude", "delegacia", "uop"]]
vehicle = df[["id_veiculo", "tipo_veiculo", "marca", "ano_fabricacao_veiculo", "id"]]
person = df[['pesid', "tipo_envolvido", "estado_fisico", "idade", "sexo", "id"]]

crash.rename(columns={"id": "crashid", "br": "code"}, inplace=True)
vehicle.rename(columns={"id": "crashid", "id_veiculo": "vehicleid"}, inplace=True)
person.rename(columns={"id": "crashid", "pesid": "personid"}, inplace=True)

crash.drop_duplicates(subset=['crashid'], inplace=True)
vehicle.drop_duplicates(subset=['vehicleid'], inplace=True)
person.drop_duplicates(subset=['personid'], inplace=True)

crash.dropna(inplace=True)
vehicle.dropna(inplace=True)
person.dropna(inplace=True)

for index, row in crash.iterrows():
    crash.at[index, "km"] = str(row["km"]).split(",")[0]
    
for index, row in vehicle.iterrows():
    vehicle.at[index, "ano_fabricacao_veiculo"] = str(row["ano_fabricacao_veiculo"]).split(".")[0]

for index, row in person.iterrows():
    person.at[index, "idade"] = str(row["idade"]).split(".")[0]
    person.at[index, "sexo"] = str(row["sexo"])[0]

crash.to_csv("finalCsv/crash.csv", index=False, header=False)
vehicle.to_csv("finalCsv/vehicle.csv", index=False, header=False)
person.to_csv("finalCsv/person.csv", index=False, header=False)

