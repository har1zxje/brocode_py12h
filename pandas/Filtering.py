import pandas as pd

df = pd.read_csv("pandas/data.csv")

tall_pkm = df[df["Height"] >= 2]
heavy_pkm = df[df["Weight"] > 100]
legend_pkm = df[df["Legendary"] == 1]#True
water_pkm = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
ff_pkm = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]

#print(tall_pkm)
#print(heavy_pkm)
#print(legend_pkm)
#print(water_pkm)
print(ff_pkm)