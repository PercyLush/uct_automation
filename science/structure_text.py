import re
import json

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\science.txt'

def aps():
    with open(path, 'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'WPS\s*of\s*(\d+)\s*or\s*above'

        aps = re.sub(pattern, r'APS: \1', data)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\science\\scienceFinal.txt', 'w', encoding='utf-8') as file2:
        file2.write(aps)    

def requirements():
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\science\\scienceFinal.txt', 'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'(Mathematics\s*\d+)\%\s*or\s*above\s*and\s*(Physical\s*Sciences\s*\d+)\%\s*or\s*above'

        requirement = re.sub(pattern, r'Requirements: \1,\2', data)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\science\\scienceFinal.txt', 'w', encoding='utf-8') as file2:
        file2.write(requirement)

def extract_key_value_pairs(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    keys_of_interest = ["APS", "Requirements"]

    extracted_data_list = []
    pattern = re.compile(r'(\w+):\s*((?:.*(?:\n(?!\w+:).*)*))\n')
    matches = pattern.findall(content)
    current_course_data = {}

    for match in matches:
        key, value = match
        if key in keys_of_interest:
            if key == "APS":
                current_course_data[key] = value.title().strip()
            if key == "Requirements":
                current_course_data[key] = value.title().strip()

        # When the "Description" key is found, consider it as the end of a course's information
        if key == "Requirements":
            extracted_data_list.append(current_course_data)
            current_course_data = {}  # Reset for the next course

    return extracted_data_list


if __name__ == '__main__':
    aps()
    requirements()

    file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\scienceFinal.txt'
    result_list = extract_key_value_pairs(file_path)

    json_file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\science\\Science.json'

    with open(json_file_path, 'w') as json_file:
        json.dump(result_list, json_file, indent=2)

    print(f"Data has been successfully stored in {json_file_path}")