import pandas as pd

df = pd.read_csv("pandas/data.csv", index_col = "Name")

#select by col
#print(df["Name"].to_string()) #select by col, return a series, to_string() de in ra toan bo series
#print(df[["Name", "Height", "Weight"]].to_string())

#select by row
#print(df.loc["Pikachu"])
#print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]])
#print(df.iloc[0:11:2, 0:3])

pokemon = input("Enter a pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found in the dataset.")