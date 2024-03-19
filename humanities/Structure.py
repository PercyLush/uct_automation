import json
import re

def structure_requirements():

    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\sample.json'

    with open(path, 'r') as file1:
        data = json.load(file1)

        for item in data:

            requirements = item['Requirements']

            pattern = r'(\d+\%\s*for\s*English\s*\(HL\)|\d+\%\s*for\s*English\s*\(FAL\)|Mathematics\s*\d+|Music\s*\d+)'

            matches = re.findall(pattern, requirements)

            item['Requirements'] = matches

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Quarter-Done.json', 'w') as file2:
        json.dump(data, file2, indent=2)

def structurise():
    
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Quarter-Done.json'

    with open(path, 'r') as file1:
        data = json.load(file1)
        
        SUBJECTS = {
                'Mathematics':'Mathematics',
                'English (HL)':'English Home Language',
                'English (FAL)':'English First Additional Language',
                'Music':'Music',
                'English \n(FAL)':'English First Additional Language'
            }

        keys_of_interest = ['Mathematics','English (HL)','English (FAL)','Music','English \n(FAL)']
        
        for item in data:
            new_requirements = ["AND"]
            requirements = item['Requirements']

            for requirement in requirements:
                pattern = r'(\d+)'
                match = re.search(pattern, requirement)
                for key in keys_of_interest:
                    if key in requirement:
                        course = {
                            "subject": SUBJECTS.get(key),
                            "minmark": int(match.group()),
                            "required": True
                        }
                        new_requirements.append(course)
                item['Requirements'] = new_requirements

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done.json', 'w') as file2:
        json.dump(data, file2, indent=2)

def final():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done.json'

    with open(path, 'r') as file1:
        data = json.load(file1)
        
        for item in data:
            english_subjects = ["OR"]
            subjects = ["AND"]
            requirements = item['Requirements']
            for requirement in requirements:
                if 'subject' in requirement:
                    if 'English' in requirement['subject']:
                        english_subjects.append(requirement)
                    else:
                        subjects.append(requirement)
                
            subjects.append(english_subjects)
            item['Requirements'] = subjects

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done2.json', 'w') as file2:
        json.dump(data, file2, indent=2)

def separator():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done2.json'

    with open(path, 'r') as file1:
        data = json.load(file1)
        new_entries = []

        for item in data:
            
            if 'Qualification' in item and ' And Bachelor' in item['Qualification']:
                new_data = item['Qualification'].split(' And ')

                item['Qualification'] = new_data[0]
                extra = {"Qualification": new_data[1], "Requirements": item['Requirements'], "FPS": item['FPS']}
                new_entries.append(extra)

        data.extend(new_entries)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done2.json', 'w') as file2:
        json.dump(data, file2, indent=2)


def clean():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\Half-Done2.json'

    with open(path, 'r') as file1:
        data = json.load(file1)
        
        for item in data:
            
            pattern = r'(\n|\s*\((.+)\)\s*)'

            if 'Qualification' in item:

                item['Qualification'] = re.sub(pattern, r'', item['Qualification'])
                item['Qualification'] = item['Qualification'].replace('  ',' ')

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\HumanitiesRequirements.json', 'w') as file2:
        json.dump(data, file2, indent=2)

def final_clean():

    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\HumanitiesRequirements.json'

    with open(path, 'r') as file1:
        data = json.load(file1)
        
            
        filtered_data = [item for item in data if not ('Qualification' in item and 'Diploma In Adult And Community Education And Training' in item['Qualification'])]


        for item in filtered_data:
            if 'FPS' in item and 'Intermediate' in item['FPS']:
                del item['FPS']

        for item1 in filtered_data:

            if 'FPS' in item1:
                item1['FPS'] = int(item1['FPS'])

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\HumanitiesRequirements.json', 'w') as file2:
        json.dump(filtered_data, file2, indent=2)

def subject_id():
    
    path2 = "C:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json"

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\HumanitiesRequirements.json', 'r') as file1, open(path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        for qualification in data1:
            for i, requirement in enumerate(qualification["Requirements"]):

                if isinstance(requirement, list) and requirement[0] == "OR":
                    for j, subj_requirement in enumerate(requirement[1:]):

                        for mapping in data2:
                            if subj_requirement.get("subject") == mapping["Name"]:
                                # Replace 'subject' with 'subjectid' from the mapping
                                subj_requirement["subjectid"] = mapping["ID"]
                                # Remove the original 'subject' key
                                del subj_requirement["subject"]
                                break

                elif "subject" in requirement:
                    for mapping in data2:
                        if requirement["subject"] == mapping["Name"]:
                            requirement["subjectid"] = mapping["ID"]
                            del requirement["subject"]
                            break

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements\\HumanitiesRequirements.json', 'w') as file:
        json.dump(data1, file, indent=2)


if __name__ == '__main__':
    structure_requirements()
    structurise()
    final()
    separator()
    clean()
    final_clean()
    subject_id()