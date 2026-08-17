import pandas as pd

df = pd.read_csv("pandas/data.csv")

#ap dung cho ca df
#print(df.mean(numeric_only = True)) #tinh mean(trung binh) cua cac cot chi la so
#print(df.sum(numeric_only = True)) #tinh sum(tong)
#print(df.min(numeric_only = True)) #tim min
#print(df.max(numeric_only = True)) #tim max
#print(df.count()) #dem so luong gtri trong tung cot

#ap dung cho 1 col
#print(df["Height"].mean()) #tinh mean(trung binh) cua cac cot chi la so
#print(df["Height"].sum()) #tinh sum(tong)
#print(df["Height"].min()) #tim min
#print(df["Height"].max()) #tim max
#print(df["Type2"].count()) #dem so luong gtri trong tung cot

group = df.groupby("Type1") #groupby theo Type1, tra ve 1 object groupby
#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
print(group["Height"].count())

