import json
import re


def main():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Half-done.json'

    with open(path,'r') as file:
        example = json.load(file)

        for item in example:
            new_data = item['Requirements'].split(', ')
            pattern = r'(Mathematics|English\s*HL|English\s*FAL)\s*(\d+)'
            subjects = ["AND"]

            english_subjects = ["OR"]

            for i in new_data:
                match = re.search(pattern, i)
                if match:
                    subject, mark = match.groups()
                    SUBJECTS = {
                        'Mathematics': 'Mathematics',
                        'English HL': 'English Home Language',
                        'English FAL': 'English First Additional Language'
                    }

                    course = {
                            "subject": SUBJECTS.get(subject),
                            "minmark": int(mark),
                            "required": True
                    }

                    if course['subject'] and course['subject'].startswith('English'):
                        english_subjects.append(course)
                    else:
                        subjects.append(course)

            subjects.append(english_subjects)
            
            item['Requirements'] = subjects

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\CommerceRequirements.json', 'w') as file2:
        json.dump(example, file2, indent=2)


def subject_id():
    qualification_data = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\CommerceRequirements.json'
    subject_id = "C:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json"

    with open(qualification_data, 'r') as data, open(subject_id, 'r') as subj_id_data:
        qual_data = json.load(data)
        data2 = json.load(subj_id_data)

        for qualification in qual_data:
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
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements\\CommerceRequirements.json', 'w') as file:
        json.dump(qual_data, file, indent=2)


if __name__ == '__main__':
    main()
    subject_id()
