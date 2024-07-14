# Python reading files (.txt, .json, .csv)

# import json

import csv

file_path = "input.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()  # txt
        # print(content)  # txt

        # content = json.load(file)  # json
        # print(content["name"])  # json

        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")
