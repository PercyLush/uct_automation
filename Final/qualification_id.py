import json
import re


qualifications = 'C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirements.json'
reference_uni = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Utility\\gradesmatch_reference.qualification2024.json'

def business_science():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:
            pattern = r'(Bachelor\s*of\s*Business\s*Science\s*specialising\s*in|Bachelor\s*of\s*Business\s*Science\s*in)'
            item['Qualification'] = re.sub(pattern, r'BBusSc', item["Qualification"])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def bachelor_commerce():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*of\s*Commerce\s*specialising\s*in|Bachelor\s*of\s*Commerce\s*in)'
            item['Qualification'] = re.sub(pattern, r'BCom', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def engineering():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*Of\s*Science\s*In\s*Engineering\s*In)'
            item['Qualification'] = re.sub(pattern, r'BScEng', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def bachelor_science():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*Of\s*Science\s*In)'
            item['Qualification'] = re.sub(pattern, r'BSc', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def bachelor_arts():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*Of\s*Arts\s*In)'
            item['Qualification'] = re.sub(pattern, r'BA', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def social_science():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*Of\s*Social\s*Science\s*In)'
            item['Qualification'] = re.sub(pattern, r'BSocSc', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def medicine():

    with open(qualifications, 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'((.+)Mbchb)'
            item['Qualification'] = re.sub(pattern, r'MBChB Medicine', item['Qualification'])

    with open(qualifications, 'w') as file:
        json.dump(data, file, indent=2)

def compare_and_append():
    with open(qualifications, 'r') as f1, open(reference_uni, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

        for item1 in data1:
            for item2 in data2:
                if item1['InstitutionID'] == item2['InstitutionID'] and item1['FacultyID'] == item2['FacultyID']:
                    if item2['Name'] in item1['Qualification']:
                        item1['QualificationID'] = item2['ID']

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'w') as file:
        json.dump(data1, file, indent=2)

def specialising():

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(specialising\s*in)'
            item['Qualification'] = re.sub(pattern, r'', item['Qualification'])

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'w') as file:
        json.dump(data, file, indent=2)

def and_():

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(\s*&\s*)'
            item['Qualification'] = re.sub(pattern, r' and ', item['Qualification'])

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'w') as file:
        json.dump(data, file, indent=2)

def bachelor_of():

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'r') as file1:
        data = json.load(file1)

        for item in data:

            pattern = r'(Bachelor\s*Of)'
            item['Qualification'] = re.sub(pattern, r'B', item['Qualification'])

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'w') as file:
        json.dump(data, file, indent=2)

def compare_and_append2():
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'r') as f1, open(reference_uni, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

        for item1 in data1:
            for item2 in data2:
                if item1['InstitutionID'] == item2['InstitutionID'] and item1['FacultyID'] == item2['FacultyID']:
                    if item2['Name'] in item1['Qualification']:
                        item1['QualificationID'] = item2['ID']

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\UctRequirementsFinal.json', 'w') as file:
        json.dump(data1, file, indent=2)

if __name__ == '__main__':
    business_science()
    bachelor_commerce()
    engineering()
    bachelor_science()
    bachelor_arts()
    social_science()
    medicine()
    compare_and_append()
    specialising()
    and_()
    bachelor_of()