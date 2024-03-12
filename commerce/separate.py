import json
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\commerce_requirements.json'

with open(path, 'r') as file1:
    data = json.load(file1)

    new_data = [new_ for new_ in data if 'Qualification' in new_]

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Semi-Final_commerce.json', 'w') as file2:
    json.dump(new_data, file2, indent=2)            