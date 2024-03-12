import PyPDF2


pdf_path = "C:\\Users\\Bheki Lushaba\\Downloads\\ug_prospectus_UCT.pdf"  # PDF file path

def main(start_page, end_page):
    text = ''

    with open(pdf_path, 'rb') as pdf:
        data = PyPDF2.PdfReader(pdf)

        for page in range(start_page - 1, end_page):

            text_file = data.pages[page]
            dattt = text_file.extract_text()
            text += dattt

    with open('UCT.txt', 'w') as file:
        file.writelines(text)


start = 30
end = 30
        
if __name__ == '__main__':
    main(start, end)
