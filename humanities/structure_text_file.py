import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanities.txt'
output_path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanitiesFinal.txt'


def clean1():
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(BACHELOR\s*OF\s*(.+)|DIPLOMA\s*(.+))'

        qualification = re.sub(pattern, r'\n\nQualification: \1' , data)

    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(qualification)

def clean2():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(Minimum requirements:)'

        requirements = re.sub(pattern, r'Requirements: ', data)

    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(requirements)

def clean3():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'WPS\s*(\d+)\s*or\s*above'

        wps = re.sub(pattern, r'WPS: \1', data)


    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(wps)

def clean4():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'FPS\s*(\d+)\s*or\s*above'

        wps = re.sub(pattern, r'FPS: \1', data)


    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(wps)

def clean5():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(ELIGIBLE BAND ADMISSION REQUIREMENTS|ELIGIBLE ADMISSION REQUIREMENTS)'
        stop = re.sub(pattern, r'Stop:', data)

    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(stop)

def clean6():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(NBT AL:)'
        stop = re.sub(pattern, r'FPS: ', data)

    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(stop)

def clean7():
    with open(output_path, 'r', encoding='utf-8') as file:
        data = file.read()

        pattern = r'(Subject requirements:(.+)\n)'

        requirements = re.sub(pattern, r'Additional: ', data)

    with open(output_path, 'w', encoding='utf-8') as file1:
        file1.write(requirements)

clean1()
clean2()
clean3()
clean4()
clean5()
clean6()
clean7()