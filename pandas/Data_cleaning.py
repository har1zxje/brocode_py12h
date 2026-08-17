import pandas as pd

# ~75% cong viec dung Pandas la de data cleaning
df = pd.read_csv("pandas/data.csv")

#1. xoa cot ko can thiet
#df = df.drop(columns = ["Legendary", "No"])

#2. xu li thieu data
#df = df.dropna(subset = ["Type2"]) #xoa nhung dong ma cot Type2 bi thieu data
#df = df.fillna({"Type2": "None"}) #thay nhung dong ma cot Type2 bi thieu data bang None

#print(df.to_string())

#3. fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire": "FIRE",
#                                   "Water": "WATER"})

#4. standardize text
#df["Name"] = df["Name"].str.lower() #chuyen tat ca cac ky tu trong cot Name ve chu thuong

#5. fix data types
#df["Legendary"] = df["Legendary"].astype(bool) #chuyen cot Legendary ve kieu bool

#6.removw duplicates values
df = df.drop_duplicates()

print(df.to_string())
