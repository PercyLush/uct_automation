import json
import os

def combine_json_files(folder_path, output_file):
    combined_data = []


    for filename in os.listdir(folder_path):

        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Assuming the file structure is a list of dictionaries, extend the combined list
                combined_data.extend(data)
    
    # Write the combined data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(combined_data, f_out, indent=4)

# Example usage
folder_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\Requirements'
output_file = 'UctRequirements.json'
combine_json_files(folder_path, output_file)
