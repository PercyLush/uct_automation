import json
import re

def combine_subjects():
    path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering(final).json'
    path2 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering(final).json'

    with open(path, 'r') as file1:
        data = json.load(file1)

    for item in data:
        subjects = []
        for key in ['Subject1', 'Subject2', 'Subject3']:
            if key in item:
                subjects.append(item[key])
                del item[key]  # Remove the original subject fields
        
        item['requirements'] = ','.join(subjects)  # Combine subjects into a single field

    with open(path2, 'w') as file1:
        json.dump(data, file1, indent=4)





if __name__ == '__main__':
    combine_subjects()
