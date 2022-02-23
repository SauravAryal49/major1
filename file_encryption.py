import PyPDF2
import docx

def read_file(filename):
    file_type=filename.split(".")

    if file_type[1] =='txt':
        content = ''
        file = open(filename, "r")
        for line in file:
            for char in line:
                content += char
        content = content+'\r'+'\n'
        return content

    if file_type[1] == 'pdf':
        print("Congratulation you are in the pdf section")
        # creating a pdf file object
        pdfFileObj = open(filename, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        content = pageObj.extractText()

        # closing the pdf file object
        pdfFileObj.close()

        return content

    if file_type[1] == 'docx':
        print("congratulation you are in the docx section")
        doc = docx.Document(filename)  # Creating word reader object.
        content = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            content = '\n'.join(fullText)

        return content


def main():
    filename = input("Enter the filename with extension:")
    file_content = read_file(filename)
    print(file_content)





if __name__ == '__main__':
    main()


