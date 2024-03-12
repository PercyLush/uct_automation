import json


path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering.json'
output_file = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\engineering(final).json'

with open(path, 'r') as file:
    data = json.load(file)

    for item in data:
        if 'Qualification' in item:
            if item['Qualification'] == 'Bachelor Of Science In Engineering In Electrical, Electrical \nAnd Computer Engineering And Mechatronics':
                item['Qualification'] = 'Bachelor Of Science In Engineering In Electrical Engineering'

                course1 = {"Qualification": 'Bachelor Of Science In Engineering In Electrical & Computer Engineering', 
                           "FPS": item['FPS'], "Subject1": item["Subject1"],
                            "Subject3": item["Subject3"]}
                course2 = {"Qualification": 'Bachelor Of Science In Engineering In Mechatronics', 
                           "FPS": item['FPS'], "Subject1": item["Subject1"],
                            "Subject3": item["Subject3"]}
                data.append(course1)
                data.append(course2)
            elif item['Qualification'] == 'Bachelor Of Science In Engineering In Mechanical, And  \nMechanical  Mechatronic Engineering':
                item['Qualification'] = 'Bachelor Of Science In Engineering In Mechanical Engineering'

                course3 = {"Qualification": 'Bachelor Of Science In Engineering In Mechanical& Mechatronics Engineering', 
                           "FPS": item['FPS'], "Subject1": item["Subject1"],
                            "Subject3": item["Subject3"]}
                
                data.append(course3)

with open(output_file, 'w') as file2:
    json.dump(data, file2, indent=2)