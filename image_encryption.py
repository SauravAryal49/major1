import io
from PIL import Image
import base64
from text_encryption import convert_to_binary,convert_to_ascii
from text_encryption import String_Split,XOR_operation
from key_generation import Crossover,mutation
import csv
from encryption import bind_key_to_message


def main(imagePath):
    im = Image.open(imagePath)
    # im = Image.open('123.jpg')
    im_resize = im.resize((500, 500))
    buf = io.BytesIO()
    im_resize.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    print(byte_im)

    byte_string = base64.b64encode(byte_im).decode("ASCII")
    print(byte_string)
    print(type(byte_string))

    ascii_value = convert_to_ascii(byte_string)
    print(ascii_value)

    binary_value = convert_to_binary(ascii_value)
    print(binary_value)

    print('Split binary array into two')
    string1, string2 = String_Split(binary_value)
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

    encrypt_message = bind_key_to_message(encrypted_message, "0100")

    print(len(encrypt_message))

    with open("img_data.csv", "w") as csvfile:
        send_file = csv.writer(csvfile)
        send_file.writerow(encrypt_message)


if __name__ == '__main__':
    print("welcome to the encryption of image")
    main()








