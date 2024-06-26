import pandas as pd

state = pd.read_csv("finalCsv/state.csv").convert_dtypes()
city = pd.read_csv("finalCsv/city.csv").convert_dtypes()
section = pd.read_csv("finalCsv/section.csv").convert_dtypes()
crash = pd.read_csv("finalCsv/crash.csv").convert_dtypes()
person = pd.read_csv("finalCsv/person.csv").convert_dtypes()
vehicle = pd.read_csv("finalCsv/vehicle.csv").convert_dtypes()

f = open("insert.sql", "w")

for index, row in state.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_state" ("state_code", "state_name") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1])
        + "');\n"
    )
for index, row in city.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_city" ("city_code", "city_name", "state_code") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1]).replace("'", '"')
        + "', '"
        + str(row[2])
        + "');\n"
    )
for index, row in section.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_section" ("section_br", "section_km", "section_date", "section_latitude", "section_longitude", "section_ic", "section_ip", "section_icm", "section_panela", "section_remendo", "section_trincamento", "section_rocada", "section_drenagem", "section_sinalizacao", "city_name") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1])
        + "', '"
        + str(row[2])
        + "', '"
        + str(row[3])
        + "', '"
        + str(row[4])
        + "', '"
        + str(row[5])
        + "', '"
        + str(row[6])
        + "', '"
        + str(row[7])
        + "', '"
        + str(row[8])
        + "', '"
        + str(row[9])
        + "', '"
        + str(row[10])
        + "', '"
        + str(row[11])
        + "', '"
        + str(row[12])
        + "', '"
        + str(row[13])
        + "', '"
        + str(row[14]).replace("'", '"')
        + "');\n"
    )
for index, row in crash.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_crash" ("crash_id", "crash_date", "crash_time", "section_br", "section_km", "crash_cause", "crash_kind", "crash_classification", "crash_day_phase", "crash_track_direction", "crash_weather", "crash_track_kind", "crash_track_layout", "crash_ground", "crash_uninjured", "crash_slightly_injured", "crash_seriously_injured", "crash_deaths", "crash_latitude", "crash_longitude", "crash_delegacy", "crash_uop") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1])
        + "', '"
        + str(row[2])
        + "', '"
        + str(row[3])
        + "', '"
        + str(row[4])
        + "', '"
        + str(row[5])
        + "', '"
        + str(row[6])
        + "', '"
        + str(row[7])
        + "', '"
        + str(row[8])
        + "', '"
        + str(row[9])
        + "', '"
        + str(row[10])
        + "', '"
        + str(row[11])
        + "', '"
        + str(row[12])
        + "', '"
        + str(row[13])
        + "', '"
        + str(row[14])
        + "', '"
        + str(row[15])
        + "', '"
        + str(row[16])
        + "', '"
        + str(row[17])
        + "', '"
        + str(row[18])
        + "', '"
        + str(row[19])
        + "', '"
        + str(row[20])
        + "', '"
        + str(row[21])
        + "');\n"
    )
for index, row in person.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_person" ("person_id", "person_kind", "person_state", "person_age", "person_sex", "crash_id") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1])
        + "', '"
        + str(row[2])
        + "', '"
        + str(row[3])
        + "', '"
        + str(row[4])
        + "', '"
        + str(row[5])
        + "');\n"
    )
for index, row in vehicle.iterrows():
    f.write(
        'INSERT INTO "bd1_accidents_vehicle" ("vehicle_id", "vehicle_kind", "vehicle_brand", "vehicle_year", "crash_id") VALUES (\''
        + str(row[0])
        + "', '"
        + str(row[1])
        + "', '"
        + str(row[2])
        + "', '"
        + str(row[3])
        + "', '"
        + str(row[4])
        + "');\n"
    )

f.close()
