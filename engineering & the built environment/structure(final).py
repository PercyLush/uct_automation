import json
import re


def main():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering(final).json'

    with open(path, 'r') as file1:
        data = json.load(file1)

        for item in data:
            pattern = r'(Mathematics|Physical Sciences|English)\s*(\d+)'
            DATA = []
            new_data = item['requirements'].split(',')

            for i in new_data:
                subject = re.search(pattern, i)
                SUBJECT = {
                    'Mathematics': 'Mathematics',
                    'Physical Sciences': 'Physical Sciences',
                    'English': 'English General'
                }

                course = {
                    "subject": SUBJECT.get(subject.group(1)),
                    "minmark": int(subject.group(2)),
                    "required": True
                }
                DATA.append(course)
            item['requirements'] = ["AND", DATA]

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\EngineeringRequirements.json', 'w') as file2:
        json.dump(data, file2, indent=2)

def final():
    path1 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\EngineeringRequirements.json'
    path2 = 'c:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json'


    with open(path1, 'r') as file1, open(path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        for item in data1:
            for sub_id in data2:
                if "requirements" in item and len(item["requirements"]) > 1:

                    for requirement in item["requirements"][1]:
                        if 'subject' in requirement:
                            if requirement['subject'] == sub_id['Name']:
                                requirement['subjectid'] = sub_id['ID']
                                del requirement['subject']


    with open(path1, 'w') as file:
        json.dump(data1, file, indent=2)


if __name__ == '__main__':
    main()
    final()


