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

    with open("img_data.csv", "w") as csvfile:
        send_file = csv.writer(csvfile)
        send_file.writerow(encrypted_message)





# value = []
# for i in binary_value:
#     data = int(i,2)
#     value.append(data)
#
#
# print("The data in the values field")
# print(value)






# decrpted_image_info=''
# for item in value:
#     character = chr(item)
#     decrpted_image_info=decrpted_image_info+character
# #
# print(decrpted_image_info)
#
# ascii_array2=decrpted_image_info.split(' ')
# print(ascii_array2)
#
# decrypted_text = ""
#
# print("checking ....")
#
# print(type(ascii_array2))
#
# for item_value in ascii_array2[1:]:
#     asciivalue=int(item_value)
#     decrypted_text += chr(asciivalue)
#
# print("final decrypted text:")
# print(decrypted_text)
#
# reverse_data = base64.b64decode(decrypted_text)
# print(reverse_data)
#
#
# img = Image.open(io.BytesIO(reverse_data))
# img.show()