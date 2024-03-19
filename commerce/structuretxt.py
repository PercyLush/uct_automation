import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce.txt'

def space():
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern1 = r'(               28      |      2024 UNDERGRADUATE PROSPECTUS)'
        datadat = re.sub(pattern1, r'', data)

        pattern = r'(BACHELOR\s*OF\s*BUSINESS\s*SCIENCE\s*AND\s*BACHELOR\s*OF\s*COMMERCE)'
        final_data = re.sub(pattern, r'\n\1', datadat)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce(structured).txt', 'w', encoding='utf-8') as file2:
        file2.write(final_data)


def whole_text():
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce(structured).txt', 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(BACHELOR\s*OF\s*BUSINESS\s*SCIENCE\s*AND\s*BACHELOR\s*OF\s*COMMERCE\s*\n(.+))'
        pattern1 = r'(WPS\s*of\s*(\d+)\s*or\s*above)'
        pattern2 = r'(Mathematics\s*\d+)'
        pattern22 = r'(English\s*HL\s*\d+)'
        pattern222 = r'(English\s*FAL\s*\d+)'
        pattern3 = r'(%)'


        data1 = re.sub(pattern, r'\nQualification: \1\n', data)
        data2 = re.sub(pattern1, r'\nWPS: \1', data1)
        data3 = re.sub(pattern2, r'Subject1: \1', data2)
        data33 = re.sub(pattern22, r'Subject2: \1', data3)
        data333 = re.sub(pattern222, r'Subject3: \1', data33)
        data4 = re.sub(pattern3, r'',data333)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce(structured).txt', 'w', encoding='utf-8') as output_file:
        output_file.write(data4)

def comment():
    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce(structured).txt', 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'Qualification:(.+)\n((.+))'

        final_data = re.sub(pattern, r'Qualification: \1\nComment: \2', data)

        pattern2 = r'Minimum required for possible admission|Only\s*SA\s*\n'
        datadata = re.sub(pattern2, r'Stop: ', final_data)

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\commerce\\Commerce(structured).txt', 'w', encoding='utf-8') as file2:
        file2.write(datadata)

space()
whole_text()
comment()