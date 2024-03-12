import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\commerce_requirements.json'

with open(path, 'r') as file:
    data = json.load(file)

    for item in data:

        pattern = r'\s*\n(.+)'
        if 'Comment' in item:
            item['Comment'] = re.sub(pattern, r'', item['Comment'])
        if 'FPS'     in item:
            item['FPS'] = re.sub(pattern, r'', item['FPS'])
        if 'Subject3' in item:
            item['Subject3'] = re.sub(pattern, r'', item['Subject3'])

with open(path, 'w') as file2:
    json.dump(data, file2, indent=2)