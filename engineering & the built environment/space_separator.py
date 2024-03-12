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

        pattern = r'(\d+)\s*(FPS\s*or\s*above\s*)'
        final_data = re.sub(pattern, r'FPS: \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject1():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'≥\s*(\d+)\s*for Mathematics'
        final_data = re.sub(pattern, r'\nSubject1: Mathematics \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject2():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'≥\s*(\d+)\s*for English'
        final_data = re.sub(pattern, r'\nSubject2: English \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

def subject3():
    with open(path2,'r', encoding='utf-8') as file1:
        data = file1.read()

        pattern = r'≥\s*(\d+)\s*for Physical Sciences'
        final_data = re.sub(pattern, r'\nSubject3: Physical Sciences \1', data)

    with open(path2, 'w', encoding='utf-8') as file2:
        file2.write(final_data)

clean()
qualification()
fps()
subject1()
subject2()
subject3()