import PyPDF2

file = 'C:\\Users\\Bheki Lushaba\\uct_automation\\ug_prospectus_10-May-2024.pdf'

def main(start_page, end_page):

    Text = ''

    with open(file, 'rb')as pdf:

        data = PyPDF2.PdfReader(pdf)

        for page in range(start_page - 1, end_page + 1):

            pages = data.pages[page]

            text = pages.extract_text()
            Text += text

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\science\\science.txt', 'w', encoding='utf-8') as file1:
        file1.write(Text)

start = 75
end = 75


if __name__ == '__main__':
    main(start, end)