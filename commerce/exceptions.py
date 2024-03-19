import json

# Define paths for ease of modification and readability.
path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\outliers.json'
path_compare = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce.json'
compare_and_append = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\commerce_requirements.json'
output_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Half-done.json'

def main():
    # Function to load JSON data from a file.
    def load_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    # Load the data from the files.
    data1 = load_json(path)
    data2 = load_json(path_compare)
    data3 = load_json(compare_and_append)

    # Initialize the list to store your results.
    data = []

    # Simplify your logic to avoid deep nesting and make it easier to follow.
    for item2 in data2:
        # Find if item2 exists in data1
        exists_in_data1 = any(item1['Qualification'].lower() == item2['Qualification'].lower() for item1 in data1)

        if not exists_in_data1:
            for item3 in data3:
                if 'except' in item3.get('Comment', '').lower():  # Ensuring 'Comment' key exists and checking 'except'.
                    course = {
                        "Qualification": item2['Qualification'],
                        "WPS": item3['WPS'],
                        "Requirements": f"{item3['Subject1']}, {item3['Subject2']}, {item3['Subject3']}"
                    }
                    data.append(course)
                    # Removed the redundant course reset as it's not needed here.

    # Write the output to a file.
    with open(output_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)


if __name__ == '__main__':
    main()

    with open(output_path, 'r') as file, open(path, 'r') as file2:
        data = json.load(file)
        data2 = json.load(file2)
        
        data.extend(data2)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Half-done.json', 'w') as file1:
        json.dump(data, file1, indent=2)