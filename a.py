import pandas as pd

section = pd.read_csv("section.csv")

for index, row in section.iterrows():
    date = str(row["date"]).split("/")
    section.at[index, "date"] = date[2] + "-" + date[0] + "-" + date[1]

section.to_csv("finalCsv/section.csv", index=False)