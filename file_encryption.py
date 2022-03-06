import PyPDF2
import docx
from encryption import convert_to_binary, convert_to_ascii, String_Split, XOR_operation, bind_key_to_message
from key_generation import Crossover, mutation
import csv


def read_file(filename):
    file_type = filename.split(".")

    if file_type[1] == 'txt':
        content = ''
        file = open(filename, "r")
        for line in file:
            for char in line:
                content += char
        content = content + '\r' + '\n'
        return content, "1100"

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

        return content, "1101"

    if file_type[1] == 'docx':
        print("congratulation you are in the docx section")
        doc = docx.Document(filename)  # Creating word reader object.
        content = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            content = '\n'.join(fullText)

        return content, "1110"


def main(filename):
    file_content, code = read_file(filename)
    print(file_content)

    print("ascii values of the file content")
    ascii_value = convert_to_ascii(file_content)

    print("binary values of the ascii value")
    binary_values = convert_to_binary(ascii_value)

    print('Split binary array into two')
    string1, string2 = String_Split(binary_values)
    print(string1)
    print(string2)

    cross_string = Crossover(string1, string2)

    print("Cross over strings ")
    print(cross_string)

    mutated = mutation(cross_string)
    print(mutated)

    mutated_string = ''.join(mutated)
    print('Mutated value')
    print(len(mutated_string))
    print(mutated_string)

    file = open("key.txt", 'r')
    key = file.read()
    print(key)

    encrypted_message = XOR_operation(mutated_string, key)
    print(len(encrypted_message))

    encrypt_message = bind_key_to_message(encrypted_message, code)

    file_type = filename.split(".")
    print(file_type)
    actual_name = file_type[0].split("/")
    print(actual_name[-1])

    with open(actual_name[-1]+".csv", "w") as csvfile:
        send_file = csv.writer(csvfile)
        send_file.writerow(encrypt_message)
        print(csvfile.name)



if __name__ == '__main__':
    main()
