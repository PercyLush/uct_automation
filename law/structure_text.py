import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\law\\law.txt'

with open(path, 'r', encoding='utf-8') as file1:
    data = file1.read()

    pattern = r'(\d+)\s*WPS\s*or\s*above'

    final_data = re.sub(pattern, r'WPS: \1', data)

with open('C:\\Users\\Bheki Lushaba\\uct_automation\\law\\lawFinal.txt', 'w', encoding='utf-8') as file2:
    file2.write(final_data)