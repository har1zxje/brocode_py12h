import pandas as pd

#la 1 mang 1 chieu, tuong tu nhu 1 cot trong excel

#data = [100, 102, 104, 200, 360]

#series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

#print(series.loc['a']) #loc la chi so cua series, loc la lay ra gia tri cua chi so a

#print(series[series < 200]) #lay ra cac gia tri nho hon 200

#vd1
# calories = {"Day 1": 1750,
#             "Day 2": 2100,
#             "Day 3": 1700}

# series = pd.Series(calories)

# series.loc["Day 3"] += 500

# #print(series.loc['Day 3']) 
# print(series[series >= 2000]) 

#hw
pal_dmg = {"Orserk": 59,
           "Solenne": 60,
           "Hartalis": 75,
           "Xenolord": 70,
           "Bellanoir Liberro": 50,
           "Blazamut Ryu": 55
           }

series = pd.Series(pal_dmg)
print(series[series >= 55]) 
