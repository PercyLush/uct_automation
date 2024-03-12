import json

# Keys of interest mapped to their specific qualification names
qualification_mapping = {
    'Actuarial Science': "Bachelor of Business Science in Actuarial Science OR Bachelor of Commerce in Actuarial Science",
    'Quantitative Finance': "Bachelor of Business Science in Actuarial Science specialising in Quantitative Finance OR Bachelor of Commerce in Actuarial Science specialising in Quantitative Finance",
    'Analytics': "Bachelor of Business Science specialising in Analytics",
    'Computer Science': "Bachelor of Business Science specialising in Computer Science",
}

key = ['ONLY', 'except']

# Placeholder path - update this path to point to your actual JSON file
path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Semi-Final_commerce.json'

with open(path, 'r') as file1:
    original_data = json.load(file1)
    filtered_data = []  # This will hold your processed data

    for item in original_data:
        for interest_key in qualification_mapping.keys():
            if key[0] in item['Comment'] and interest_key in item['Comment']:
                # Use the mapped qualification name for the interest key
                qualification_name = qualification_mapping[interest_key]
                
                # Construct the course dictionary
                course = {
                    "Qualification": qualification_name,
                    "FPS": item['FPS'],
                    "Requirements": f"{item['Subject1']}, {item['Subject2']}, {item['Subject3']}"
                }
                filtered_data.append(course)
                # Note: The logic for 'except' or handling the second item in 'key' is not clear from your code, so it's not included here.

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\ToCleanCommerce.json', 'w') as file2:
    json.dump(filtered_data, file2, indent=2)

