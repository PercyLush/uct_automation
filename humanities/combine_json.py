import json

json1 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanities.json'
json2 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanities2.json'

with open(json1, 'r') as file1, open(json2, 'r') as file2:

    data1 = json.load(file1)
    data2 = json.load(file2)

    for item1 in data1:
        for item2 in data2:

            if 'Qualification' in item1:

                if item1['Qualification'] == item2['Qualification']:
                    if 'Additional' in item2:
                        item1['Requirements'] = item1['Requirements'] + item2['Additional']

    data1 = [new_ for new_ in data1 if 'Qualification' in new_]

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\sample.json', 'w') as file:
    json.dump(data1, file, indent=2)
