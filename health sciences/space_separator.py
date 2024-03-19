import re

path1 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\health.txt'
path2 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\health(final).txt'


def clean():

    with open(path1, 'r') as file1:
        data = file1.read()

        pattern = r'%'

        final_data = re.sub(pattern, r'' , data)

    with open(path2, 'w') as file2:
        file2.write(final_data)


def qualification():

    with open(path2, 'r') as file1:
        data = file1.read()

        pattern = r'(BACHELOR OF MEDICINE|BACHELOR OF SCIENCE)(.+)'

        final_data = re.sub(pattern, r'\n\nQualification: \1\2' , data)

    with open(path2, 'w') as file2:
        file2.write(final_data)


def fps():

    with open(path2, 'r') as file1:
        data = file1.read()

        pattern = r'(\d+)\s*WPS\s*or\s*above'

        final_data = re.sub(pattern, r'WPS: \1' , data)

    with open(path2, 'w') as file2:
        file2.write(final_data)

def requirements():

    with open(path2, 'r') as file1:
        data = file1.read()

        pattern = r'Minimum subject requirements and performance levels to be considered for admission:'

        final_data = re.sub(pattern, r'Requirements: ' , data)

    with open(path2, 'w') as file2:
        file2.write(final_data)

def extra():

    with open(path2, 'r') as file1:
        data = file1.read()

        pattern = r'ELIGIBLE\s*BANDS\s*ADMISSION\s*REQUIREMENTS|Meet\s*minimum\s*subject\s*requirements\s*|;'

        final_data = re.sub(pattern, r'\nExtra: ' , data)

    with open(path2, 'w') as file2:
        file2.write(final_data)

clean()
qualification()
fps()
requirements()
extra()