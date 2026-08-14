import json
import csv 

#TXT
#file_path = "output.txt"

#try:
#    with open(file_path, "r") as file:
#        content = file.read()
#        print(content)
#except FileNotFoundError:
#    print("That file was not found")
#except PermissionError:
#    print("U do not have permission to read this file")

#JSON
#file_path = "output.json"

#try:
#    with open(file_path, "r") as file:
#        content = json.load(file)
#        print(content["name"])
#except FileNotFoundError:
#    print("That file was not found")
#except PermissionError:
#    print("U do not have permission to read this file")

#CSV
file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("U do not have permission to read this file")