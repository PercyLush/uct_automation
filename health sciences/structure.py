import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\health(tease).json'

def main():

    with open(path, 'r') as file:
        data = json.load(file)

        final_data = [new_ for new_ in data if 'Qualification' in new_]

    with open(path, 'w') as file2:
        json.dump(final_data, file2, indent=2)


def clean():

    with open(path, 'r') as file:
        data = json.load(file)

        pattern = r'\n|at '

        for item in data:
            if 'Requirements' in item:
                item['Requirements'] = re.sub(pattern, r'', item['Requirements'])

    with open(path, 'w') as file2:
        json.dump(data, file2, indent=2)

    
def clean2():

    with open(path, 'r') as file:
        data = json.load(file)

        pattern = r'\s*-\s*|\s*\n'

        for item in data:
            if 'Requirements' in item:
                item['Requirements'] = re.sub(pattern, r'', item['Requirements'])

    with open(path, 'w') as file2:
        json.dump(data, file2, indent=2)

def structure():

    keys_of_interest = ['Mathematics', 'Physical Sciences', 'English (Home or First Additional Language)', 'Life Sciences']

    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\health(tease).json'
    DATA = []

    with open(path, 'r') as file:
        data = json.load(file)

        for item in data:
            requirements = item['Requirements']
            new_data = requirements.split(', ')

            DATA = ["AND"]
            for key in keys_of_interest:
                for i in new_data:
                    if i.startswith(key):
                        pattern = r'(.+)\s*(\d{2})'
                        mark = re.search(pattern, i)
                        course = {"subject": mark.group(1).strip(),
                                  "minmark": int(mark.group(2).strip()),
                                "required": True
                                  }
                        DATA.append(course)
                item['Requirements'] = DATA

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\Semi-Done.json', 'w') as file1:
        json.dump(data, file1, indent=2)


if __name__ == '__main__':
    main()
    clean()
    clean2()
    structure()