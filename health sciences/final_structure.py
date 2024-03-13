import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\Semi-Done.json'
output_file = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\HealthScienceRequirements.json'

def main():
    
    with open(path, 'r') as file1:
        data = json.load(file1)


        for item in data:
            requirements = item['Requirements']

            AND_DATA = ['AND', []]
            for requirement in requirements:
                if 'subject' in requirement:
                    # To separate AND subjects
                    if ' and ' in requirement['subject']:
                        new_data = requirement['subject'].split(' and ')
                        for subject in new_data:
                            course = {
                                "subject": subject,
                                "minmark": int(requirement['minmark'])
                            }
                            AND_DATA[1].append(course)
                    # To separate OR subjects
                    elif ' or ' in requirement['subject']:
                        new_data = requirement['subject'].split(' or ')

                        SUBJECT = {
                            'English (Home': 'English Home Language',
                            'First Additional Language)': 'English First Additional Language',
                            'Mathematics': 'Mathematics',
                            'Mathematical Literacy': 'Mathematical Literacy',
                            'Life Sciences': 'Life Sciences',
                            'Physical Sciences': 'Physical Sciences'
                        }
                        or_data = []
                        for subject in new_data:
                            pattern = r'(.+)\s*(\d{2})'
                            match = re.search(pattern, subject)
                            if match:
                                course = {
                                    "subject": match.group(1).strip(),
                                    "minmark": int(match.group(2))
                                }
                            else:
                                course = {
                                    "subject": SUBJECT.get(subject.strip(), subject),
                                    "minmark": int(requirement['minmark'])
                                }
                            or_data.append(course)
                        AND_DATA[1].append(["OR", or_data])
                    # For requirements without 'and' or 'or' directly appended to AND_DATA
                    else:
                        AND_DATA[1].append(requirement)
            item['Requirements'] = AND_DATA


    with open(output_file, 'w') as file2:
        json.dump(data, file2, indent=2)

def subject_id():
    
    path2 = "C:\\Users\\Bheki Lushaba\\Downloads\\gradesmatch_reference.subject.json"
    with open(output_file, 'r') as file1, open(path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        for item in data1:
            for sub_id in data2:

                for req in item["Requirements"]:
                    for _and in req['AND']:

                        if 'OR' in _and:
                            for _or in _and['OR']:
                                if 'subject' in _or:
                                    if _or['subject'] == sub_id['Name']:

                                        _or['subject'] = sub_id['ID']
                                        _or['subjectid'] = _or.pop('subject')
                                        
                        elif _and['subject'] == sub_id['Name']:

                            _and['subject'] = sub_id['ID']
                            _and['subjectid'] = _and.pop('subject')

                        else:
                            if 'subject' in _and:
                                if _and['subject'] == sub_id['Name']:

                                    _and['subject'] = sub_id['ID']
                                    _and['subjectid'] = _and.pop('subject')


    with open('testing.json', 'w') as file:
        json.dump(data1, file, indent=2)


if __name__ == '__main__':
    main()
    subject_id()
