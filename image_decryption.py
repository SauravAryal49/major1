from key_generation import Crossover,mutation
from text_decryption import convert_to_eight,convert_to_list,binary_array,setnetwork,train_network,XOR_operation
import base64
from PIL import Image
import io



file_name = open('data1.csv', 'r')
encrypted_data = file_name.read()
encrypted = ''
for i in range(0, len(encrypted_data)):
    if not encrypted_data[i] == ',':
        encrypted += encrypted_data[i]

encrypted = encrypted.rstrip()
print("obtained values")
print(encrypted)
file = open("key.txt", 'r')
key = file.read()
print("key values")
print(key)

first_level_decryption = XOR_operation(encrypted, key)
print('separation from the key')
print(first_level_decryption)

dataset = convert_to_eight(first_level_decryption)
print('values in the segments of 8')
print(dataset)
print(len(dataset))

cipher = binary_array(dataset)
print(cipher)

datasets = convert_to_list(dataset, cipher)

print(datasets)

# trying out to decrypt from here

n_inputs = 8
n_outputs = 255

network = setnetwork(n_inputs, 2, n_outputs)
error = train_network(network, datasets, 0.2, 5000, n_outputs)

ascii_array = []
# first conversion of ascii value
if error < 0.19:
    for item  in cipher:
        ascii_array.append(item)
else:
    print("Error")

print("first Ascii conversion[array]:")
print(ascii_array)


#second conversion to asccii value
strb=""
ascii_array1 = []
for item in ascii_array:
    character = chr(item)
    ascii_array1.append(character)
    strb=strb+character
print("First Ascii conversion:")
print(strb)
print("==========================================================")
print("Second ascii conversion:[array]")
print(ascii_array1)



decrypted_text = ""
ascii_array2 = strb.split(' ')
ascii_array2.pop(0)
print(ascii_array2)
print(type(ascii_array2))

for item in ascii_array2:
    asciivalue=int(item)
    decrypted_text += chr(asciivalue)
print("final decrypted text:")
print(decrypted_text)


reverse_data = base64.b64decode(decrypted_text)
print(reverse_data)


img = Image.open(io.BytesIO(reverse_data))
img.show()



