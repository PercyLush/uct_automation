import PyPDF2
import re

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\ug_prospectus_10-May-2024.pdf'


def main(start_page, end_page):
    Text = ""

    with open(path, 'rb') as pdf:
        data = PyPDF2.PdfReader(pdf)

        for page in range(start_page - 1, end_page + 1):

            text = data.pages[page]
            extract = text.extract_text()
            Text += extract

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\health sciences\\health.txt', 'w', encoding='utf-8') as file:
        file.write(Text)


start = 45
end = 47

if __name__ == '__main__':
    main(start, end)
    print('Extracted!')