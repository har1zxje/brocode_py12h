weight = float(input("enter ur weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"ur weight is: {round(weight,2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"ur weight is: {round(weight,2)} {unit}")
else: 
    print(f"{unit} was not valid")

