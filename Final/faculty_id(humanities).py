import json
import re

faculty_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements\\HumanitiesRequirements.json'


def institute():
    references = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Utility\\gradesmatch_reference.institution2024.json'

    with open(faculty_path, 'r') as file1, open(references, 'r', encoding='utf-8') as ref:

        data = json.load(file1)
        REF = json.load(ref)

        for item in data:
            for Reference in REF:

                if Reference['Name'] == 'University of Cape Town':
                    item['InstitutionID'] = Reference['ID']


    with open(faculty_path, 'w') as file:
        json.dump(data, file, indent=2)


def faculty():
    references = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Utility\\gradesmatch_reference.faculty2024.json'

    with open(faculty_path, 'r') as file1, open(references, 'r', encoding='utf-8') as ref:

        data = json.load(file1)
        REF = json.load(ref)

        for item in data:
            for Reference in REF:

                if item['InstitutionID'] == Reference['InstitutionID'] and Reference["Name"] == "Humanities" :#Faculty Name
                    item["FacultyID"] = Reference["ID"]
                    


    with open(faculty_path, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == '__main__':
    institute()
    faculty()