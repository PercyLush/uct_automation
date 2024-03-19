import json


path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science.json'

with open(path, 'r', encoding='utf-8') as file1:
    data = json.load(file1)
    DATA = []

    for item in data:

        new_data = item.split('\n')

        for n in new_data:
            course = {"Qualification": f"BSc {n}"}
            DATA.append(course)

        additionl = {"Qualification": "Bachelor of Science"}
        DATA.append(additionl)

with open(path, 'w') as file2:
    json.dump(DATA, file2, indent=2)