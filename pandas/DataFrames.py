import pandas as pd

#la 1 mang 2 chieu, tuong tu nhu 1 bang trong excel

# data = {"Name": ["Spongbob", "Patrick", "Squidward"],
#         "Age": [30, 35, 50]}

# df = pd.DataFrame(data, index = ["Emp1", "Emp2", "Emp3"]) #index la chi so cua dataframe, tuong tu Series

#print(df.loc["Emp1"])
#print(df.iloc[0]) #loc de tim theo ten index, iloc de tim theo chi so index

#add new col
# df["Job"] = ["Cook", "N/A", "Cashier"]
# print(df)

#add new rows
# new_row = pd.DataFrame(
#     [{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
#      {"Name": "Eugene", "Age": 60, "Job": "Manager"}], index = ["Emp4", "Emp5"])
# df = pd.concat([df, new_row]) #su dung concat de noi chuoi 2 dataframe lai voi nhau, df la dataframe cu, new_row la dataframe moi, index la chi so cua dataframe moi
# print(df)

#hw
data = {"Name": ["Hai", "Quang", "Dang", "Duong"],
        "Hometown": [23, 36, 22, 12],
        "Job": ["N/A", "FE", "FS", "FE"]}

df = pd.DataFrame(data, index = ["No1", "No2", "No3", "No4"])


df["KDA"] = [2.3, 1.3, 0.9, 1.5]


new_player = pd.DataFrame([{"Name": "Minh", "Hometown": 99, "Job": "Cashier", "KDA": 1.8}], index = ["No5"])

df = pd.concat([df, new_player])
print(df)
