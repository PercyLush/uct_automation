import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json'
output_file = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering(final).json'


def clean():
    with open(path, 'r') as file:
        data = json.load(file)

        for item in data:
            if 'Qualification' in item:
                pattern = r'\n\d+(.+)|\n\u2265(.+)|\nAll Applicantsband B\nWpsprobable Admission|\nArchitecture Portfolio Score Of 75 Or Above'
                item['Qualification'] = re.sub(pattern, r'', item['Qualification'])

    with open(path, 'w') as file2:
        json.dump(data, file2, indent=2)


def separate():
    with open(path, 'r') as file:
        data = json.load(file)

        for item in data:
            if 'Qualification' in item:
                if item['Qualification'] == 'Bachelor Of Science In Engineering In Electrical, Electrical \nAnd Computer Engineering And Mechatronics':
                    item['Qualification'] = 'Bachelor Of Science In Engineering In Electrical Engineering'

                    course1 = {"Qualification": 'Bachelor Of Science In Engineering In Electrical & Computer Engineering', 
                            "WPS": int(item['WPS']), "Subject1": item["Subject1"],
                                "Subject3": item["Subject3"]}
                    course2 = {"Qualification": 'Bachelor Of Science In Engineering In Mechatronics', 
                            "WPS": int(item['WPS']), "Subject1": item["Subject1"],
                                "Subject3": item["Subject3"]}
                    data.append(course1)
                    data.append(course2)
                elif item['Qualification'] == 'Bachelor Of Science In Engineering In Mechanical, And  \nMechanical  Mechatronic Engineering':
                    item['Qualification'] = 'Bachelor Of Science In Engineering In Mechanical Engineering'

                    course3 = {"Qualification": 'Bachelor Of Science In Engineering In Mechanical& Mechatronics Engineering', 
                            "WPS": int(item['WPS']), "Subject1": item["Subject1"],
                                "Subject3": item["Subject3"]}
                    
                    data.append(course3)

    with open(output_file, 'w') as file2:
        json.dump(data, file2, indent=2)

if __name__ == '__main__':
    clean()
    separate()