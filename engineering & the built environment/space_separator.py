import re

path1 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\ebe.txt'
path2 = 'C:\\Users\\Bheki Lushaba\\uct_automation\\engineering & the built environment\\ebe(final).txt'

def clean():
    with open(path1,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'(;|%|\s*NSC\s*|&)'
        final_data = re.sub(pattern, r'', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)


def qualification():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'(BACHELOR\s*OF(.+))'
        final_data = re.sub(pattern, r'\n\nQualification: \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def fps():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'(\d+)\s*(WPS\s*or\s*above\s*)'
        final_data = re.sub(pattern, r'WPS: \1\n', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject1():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'WPS:\s*(\d+)\n≥\s*(\d+)\s*for\s*Mathematics'
        final_data = re.sub(pattern, r'WPS: \1\nSubject1: Mathematics \2', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject2():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'Subject1:\s*(Mathematics\s*\d+)\s*≥\s*(\d+)\s*for\s*English'
        final_data = re.sub(pattern, r'Subject1: \1\nSubject2: English \2', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject3():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'Subject1:\s*(Mathematics\s*\d+)\s*≥\s*(\d+)\s*for\s*Physical\s*Sciences'
        final_data = re.sub(pattern, r'Subject1: \1\nSubject3: Physical Sciences \2', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def stop():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'Only\s*SA(.+)'
        final_data = re.sub(pattern, r'Stop: \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

clean()
qualification()
fps()
subject1()
subject2()
subject3()
stop()