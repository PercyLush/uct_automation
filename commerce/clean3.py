import json

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\ToCleanCommerce.json', 'r') as file3:
    data1 = json.load(file3)

    for item in data1:

        if 'Qualification' in item:

            if ' OR ' in item['Qualification']:
                new_data = item['Qualification'].split(' OR ')
                item['Qualification'] = new_data[0]
                course = {"Qualification": new_data[1], "WPS": item['WPS'], "Requirements": item['Requirements']}
                data1.append(course)
            else:
                pass

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\outliers.json', 'w') as file3:
    json.dump(data1, file3, indent=2)