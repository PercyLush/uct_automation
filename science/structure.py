import json
import re

def clean():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\Science.json'

    with open(path, 'r', encoding='utf-8') as file1:
        data = json.load(file1)

        new_data = [sus for sus in data if "APS" in sus]

        for item in new_data:

            item['Requirements'] = re.sub(r'(\s*\n(.+))', r'', item['Requirements'])

    with open(path, 'w', encoding='utf-8') as file2:
        json.dump(new_data, file2, indent=2)

def structure():

    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\Science.json'
    keys_of_interests = ["Mathematics", "Physical Sciences"]

    with open(path, 'r', encoding='utf-8') as file1:
        data = json.load(file1)

        for item in data:
            subjects = item["Requirements"].split(',')
            DATA = ["AND"]

            for key in keys_of_interests:
                for subject in subjects:
                    if key in subject:
                        pattern = r'(\d+)'
                        match = re.search(pattern, subject)
                        course = {"subject": key, "minmark": int(match.group()), "required": True}
                        DATA.append(course)

            item['APS'] = int(item['APS'])
            item['Requirements'] = DATA

    with open("C:\\Users\\Bheki Lushaba\\uct_automation\\science\\ScienceRequirements.json", 'w') as file2:
        json.dump(data, file2, indent=2)

def append():

    qualification = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science.json'
    requirement = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\ScienceRequirements.json'

    with open(requirement, 'r') as req, open(qualification, 'r') as qual:
        require = json.load(req)
        qualif = json.load(qual)

        for item in qualif:
            if "Qualification" in item:
                item["Requirements"] = require[0]["Requirements"]
                item["APS"] = require[0]["APS"]

    with open("C:\\Users\\Bheki Lushaba\\uct_automation\\science\\ScienceRequirements.json", 'w') as file:
        json.dump(qualif, file, indent=2)

def subject_id():
    
    path2 = "C:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json"

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\science\\ScienceRequirements.json', 'r') as file1, open(path2, 'r') as file2:
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

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements\\ScienceRequirements.json', 'w') as file:
        json.dump(data1, file, indent=2)

if __name__ == '__main__':
    clean()
    structure()
    append()
    subject_id()