import PyPDF2

path = 'C:\\Users\\Bheki Lushaba\\uct_automation\\ug_prospectus_10-May-2024.pdf'

def main(start_page, end_page):
    with open(path, 'rb') as file:

        data = PyPDF2.PdfReader(file)

        Text = ""

        for page in range(start_page - 1, end_page + 1):

            pages = data.pages[page]

            text = pages.extract_text()
            Text += text

    with open('C:\\Users\\Bheki Lushaba\\uct_automation\\humanities\\humanities.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(Text)


start = 59 #Page number you want to start extracting
end = 61 #Page number you want to stop extracting

if __name__ == '__main__':
    main(start, end)