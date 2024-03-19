import json
import re

def clean():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json'

    with open(path, 'r') as file1:
        data = json.load(file1)

        for item in data:

            if 'Qualification' in item:
                pattern = r'(\s*\nMinimum Requirements:(.+)\n(.+)\n(.+)\n(.+)\n(.+)|s*\nMinimum Requirements:\n(.+)\n(.+)\n(.+)\n(.+))'
                item['Qualification'] = re.sub(pattern, r'',item['Qualification'])


            if 'Subject1' in item:
                pattern = r'(\s*\n(.+))'
                item['Subject1'] = re.sub(pattern, r'',item['Subject1'])


            if 'Subject2' in item:
                pattern = r'(\s*\n(.+))'
                item['Subject2'] = re.sub(pattern, r'',item['Subject2'])


            if 'Subject3' in item:
                pattern = r'(\s*\n(.+))'
                item['Subject3'] = re.sub(pattern, r'',item['Subject3'])

    with open(path, 'w') as file2:
        json.dump(data, file2, indent=2)

def structure():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json'

    with open(path, 'r') as file1:
        data = json.load(file1)

        new_data = [new_ for new_ in data if 'Qualification' in new_]

    with open(path, 'w') as file2:
        json.dump(new_data, file2, indent=2)


if __name__ == '__main__':
    clean()
    structure()