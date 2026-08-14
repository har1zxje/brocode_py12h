unit = input("Celsius or Fahrenheit (C or F): ")
temp = float(input("enter ur temperature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "'F"
    print(f"ur temperature is: {round(temp,2)} {unit}")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    unit = "'C"
    print(f"ur temperature is: {round(temp,2)} {unit}")
else: 
    print(f"{unit} was not valid")
