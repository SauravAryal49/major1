from encryption import bind_key_to_message,convert_to_ascii,convert_to_binary,XOR_operation,String_Split
import csv
from key_generation import Crossover, mutation


def text_input():
    string = input("Enter the plain text")
    return string.strip()


def main(message):
    print('Welcome to the encryption part')
    string = message

    print("The ascii values of the text values ")
    ascii_value = convert_to_ascii(string)
    print(ascii_value)

    print("binary values of the ascii value")
    binary_values = convert_to_binary(ascii_value)
    print(binary_values)

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

    encrypt_message = bind_key_to_message(encrypted_message, "0000")


    with open("text_data.csv", "w") as csvfile:
        send_file = csv.writer(csvfile)
        send_file.writerow(encrypt_message)




if __name__ == '__main__':
    print("my name is saurav")
    main()
