import json
import re

def main():
    path1 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\ebe1.json'
    path2 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\ebe2.json'

    with open(path1, 'r') as file1, open(path2, 'r') as file2:
        
        data1 = json.load(file1)
        data2 = json.load(file2)

        for item2 in data2:
            if "Qualification" in item2:
                if 'Bachelor Of Science In Property Studies' in item2['Qualification']:
                    data1.append(item2)
                else:
                    pass


    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json', 'w') as file:
        json.dump(data1, file, indent=2)

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
    main()
    clean()
    structure()