import json
import csv

#mode:
#w: write du ton tai hay ko
#x: tao file neu chua ton tai, ton tai se bao loi
#a: append them data vao file

#TXT
#txt_data = "I LIKE VALORANT"
#file_path = "output.txt"
#try:
#    with open(file = file_path, mode = "w") as file:
#        file.write(txt_data)
#        print(f"txt file {file_path} was created")
#except FileExistsError:
#    print("That file already exist!")

#JSON
#employee = {
#    "name": "Spongebob",
#    "age": 30,
#    "job": "cook"
#}

#file_path = "output.json"
#try:
#    with open(file = file_path, mode = "w") as file:
#        json.dump(employee, file, indent=4)
#        print(f"json file {file_path} was created")
#except FileExistsError:
#    print("That file already exist!")

#CSV
employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]
file_path = "output.csv"
try:
    with open(file = file_path, mode = "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exist!")