import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\commerce_requirements.json'

with open(path, 'r') as file1:
    data = json.load(file1)

    for item in data:

        if 'WPS' in item:

            pattern = r'(\d+)'
            matches = re.search(pattern, item['WPS'])
            item['WPS'] = int(matches.group())

        if 'Subject3' in item:

            pattern1 = r'(\s*\((.+)\))'
            item['Subject3'] = re.sub(pattern1, r'', item['Subject3'])

    data = [new_ for new_ in data if 'Qualification' in new_]

with open(path, 'w') as file2:
    json.dump(data, file2, indent=2)            