import pandas as pd
import requests as rq
import numpy as np

section = pd.read_csv("partialCsv/section.csv")

brant = 0
kmant = 0

for index, row in section.iterrows():
    km = int(row["km"])
    br = int(row["code"])
    if km - kmant < 10 and br == brant:
        section.at[index, "cityname"] = section.at[index-1, "cityname"]
        continue
    lat = row["Latitude"]
    long = row["Longitude"]
    data = rq.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&sensor=true&key=AIzaSyDqAA19uaTBjC-AtzcvcJGL4LDDLn_aGmg".format(lat=lat, long = long)).json()
    try: 
        comps = data["results"][0]["address_components"]
        city = "."
        for comp in comps:
            if "administrative_area_level_2" in comp["types"]:
                city = comp["long_name"]
                break
    except: 
        city = "."
    section.at[index, "cityname"] = city
    kmant = km
    brant = br
    print(str(index)+city)
    
section.replace({".": np.nan}, inplace=True)

section.dropna(inplace=True)

section.drop(columns=["stateid"], inplace=True)

for index, row in section.iterrows():
    date = str(row["Data"]).split("/")
    section.at[index, "Data"] = date[2] + "-" + date[0] + "-" + date[1]
    
section.to_csv("finalCsv/section.csv", index=False)
