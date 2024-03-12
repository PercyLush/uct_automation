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
                    "Subjects": f"{item['Subject1']}, {item['Subject2']}, {item['Subject3']}"
                }
                filtered_data.append(course)
                # Note: The logic for 'except' or handling the second item in 'key' is not clear from your code, so it's not included here.

with open('ToCleanCommerce.json', 'w') as file2:
    json.dump(filtered_data, file2, indent=2)


with open('C:\\Users\\Bheki Lushaba\\uct_automation\\ToCleanCommerce.json', 'r') as file3:
    data1 = json.load(file3)

    for item in data1:

        if 'Qualification' in item:

            if ' OR ' in item['Qualification']:
                new_data = item['Qualification'].split(' OR ')
                item['Qualification'] = new_data[0]
                course = {"Qualification": new_data[1], "FPS": item['FPS', "Subjects": item['Subjects']]}
                data1.append(course)
            else:
                pass

with open('testing.json', 'w') as file3:
    json.dump(data1, file3, indent=2)
