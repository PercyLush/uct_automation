import re
import json

def extract_key_value_pairs(file_path):
    import re
    # Open the file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the keys you're interested in
    keys_of_interest = ["Qualification", "Comment", "WPS","Subject1","Subject2","Subject3"]

    # Initialize a list to store JSON objects for each course
    extracted_data_list = []

    # Regular expression pattern to match key-value pairs
    pattern = re.compile(r'(\w+):\s*((?:.*(?:\n(?!\w+:).*)*))\n')

    # Find all matches in the content
    matches = pattern.findall(content)

    # Initialize a dictionary to store key-value pairs for the current course
    current_course_data = {}

    # Iterate over matches and store JSON objects for each course in the list
    for match in matches:
        key, value = match
        if key in keys_of_interest:
            if key == "Qualification":
                current_course_data[key] = value.title().strip()

            if key == "WPS":
                current_course_data[key] = value.strip()

            if key == "Subject1":
                current_course_data[key] = value.strip()

            if key == "Subject2":
                current_course_data[key] = value.strip()

            if key == "Subject3":
                current_course_data[key] = value.strip()

        
        # When the "Description" key is found, consider it as the end of a course's information
        
        if key == "Stop":
            extracted_data_list.append(current_course_data)
            current_course_data = {}  # Reset for the next course
            

    return extracted_data_list

# Provide the path to your text file
file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\ebe(final).txt'

# Call the function to extract key-value pairs
result_list = extract_key_value_pairs(file_path)

# Specify the path for the JSON file
json_file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json'

# Write the list of JSON objects to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(result_list, json_file, indent=2)

print(f"Data has been successfully stored in {json_file_path}")
