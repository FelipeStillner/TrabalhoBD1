import pandas as pd

df = pd.read_csv("initialCsv/prf2023agrpesstodas.csv", encoding='latin-1', on_bad_lines='skip', sep=";")

crash = df[["id", "data_inversa", "dia_semana", "horario", "uf", "br", "km", "municipio", "causa_principal", "causa_acidente", "ordem_tipo_acidente", "tipo_acidente", "classificacao_acidente", "fase_dia", "sentido_via", "condicao_metereologica", "tipo_pista", "tracado_via", "uso_solo", "ilesos", "feridos_leves", "feridos_graves", "mortos", "latitude", "longitude", "regional", "delegacia", "uop"]]
vehicle = df[["id_veiculo", "tipo_veiculo", "marca", "ano_fabricacao_veiculo", "id"]]
person = df[['pesid', "tipo_envolvido", "estado_fisico", "idade", "sexo", "id"]]

crash.rename(columns={"id": "crashid"}, inplace=True)
vehicle.rename(columns={"id": "crashid", "id_veiculo": "vehicleid"}, inplace=True)
person.rename(columns={"id": "crashid", "pesid": "personid"}, inplace=True)

crash.drop_duplicates(subset=['crashid'], inplace=True)
vehicle.drop_duplicates(subset=['vehicleid'], inplace=True)
person.drop_duplicates(subset=['personid'], inplace=True)

crash.dropna(inplace=True)
vehicle.dropna(inplace=True)
person.dropna(inplace=True)

crash.to_csv("finalCsv/crash.csv", index=False)
vehicle.to_csv("finalCsv/vehicle.csv", index=False)
person.to_csv("finalCsv/person.csv", index=False)

