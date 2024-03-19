import re
import json

def extract_key_value_pairs(file_path):
    import re
    # Open the file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the keys you're interested in
    keys_of_interest = ["Qualification", "Requirements", "WPS", "FPS", "Additional"]

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
        # Only process keys of interest
        if key in keys_of_interest:
            # Special processing for 'Qualification'
            if key == "Qualification":
                current_course_data[key] = value.title().strip()
            else:
                current_course_data[key] = value.strip()

        # Add the current course to the list when a course-ending condition is met
        if (key == "Additional") or  key == "FPS":
            extracted_data_list.append(current_course_data)
            current_course_data = {}  # Reset for the next course

    # Handle the case where the last course might not end with 'FPS' or 'Additional Requirements'
    if current_course_data:
        extracted_data_list.append(current_course_data)

    return extracted_data_list

# Provide the path to your text file
file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanitiesFinal.txt'

# Call the function to extract key-value pairs
result_list = extract_key_value_pairs(file_path)

# Specify the path for the JSON file
json_file_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanities.json'

# Write the list of JSON objects to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(result_list, json_file, indent=2)

print(f"Data has been successfully stored in {json_file_path}")
