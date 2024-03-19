import json
import re

path_pdf = 'C:\\Users\\Bheki Lushaba\\uct_automation\\law\\law.json'
path_scrpe = 'C:\\Users\\Bheki Lushaba\\uct_automation\\law.json'
output_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements\\LawRequirements.json'

def clean():
    with open(path_pdf, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for item1 in data:
            
            pattern = r'(\n(.+))'
            item1['WPS'] = re.sub(pattern, r'', item1['WPS'])

    with open(path_pdf, 'w') as file2:
        json.dump(data, file2, indent=2)

def structure():
    with open(path_pdf, 'r') as file1, open(path_scrpe, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        for item1 in data1:
            for item2 in data2:
                if 'Qualification' in item2:
                    if 'WPS' in item1:
                        item2['APS'] = int(item1['WPS'])

    with open(output_path, 'w') as file:
        json.dump(data2, file, indent=2)

if __name__ == '__main__':
    clean()
    structure()