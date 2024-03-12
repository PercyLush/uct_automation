import json
import re


def main():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Half-done.json'

    with open(path,'r') as file:
        example = json.load(file)

        for item in example:
            new_data = item['Requirements'].split(', ')
            pattern = r'(Mathematics|English\s*HL|English\s*FAL)\s*(\d+)'
            subjects = []

            english_subjects = []
            other_subjects = []

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
                        other_subjects.append(course)

            # Assuming you want to apply "OR" logic to English subjects and list everything under "AND"
            if english_subjects:
                subjects.append({"OR": english_subjects})
            subjects.extend(other_subjects)  # Add non-English subjects directly
            
            item['Requirements'] = [{"AND": subjects}]

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\CommerceRequirements.json', 'w') as file2:
        json.dump(example, file2, indent=2)


def main1():
    qualification_data = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\CommerceRequirements.json'
    subject_id = "C:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json"

    with open(qualification_data, 'r') as data, open(subject_id, 'r') as subj_id_data:
        qual_data = json.load(data)
        subj_id = json.load(subj_id_data)

        for item in qual_data:
            for sub_id in subj_id:

                for req in item["Subjects"]:
                    for _and in req['AND']:

                        if 'OR' in _and:
                            for _or in _and['OR']:
                                if 'subject' in _or:
                                    if _or['subject'] == sub_id['Name']:

                                        _or['subject'] = sub_id['ID']
                                        _or['subjectid'] = _or.pop('subject')
                        else:
                            if 'subject' in _and:
                                if _and['subject'] == sub_id['Name']:

                                    _and['subject'] = sub_id['ID']
                                    _and['subjectid'] = _and.pop('subject')
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\CommerceRequirements.json', 'w') as file:
        json.dump(qual_data, file, indent=2)


if __name__ == '__main__':
    main()
    main1()
