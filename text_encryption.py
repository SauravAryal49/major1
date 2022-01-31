import random
import math
import sympy
import csv
from key_generation import Crossover, mutation


def convert_to_ascii(Strings):
    ascii_value = []
    for c in Strings:
        a = str(ord(c))
        # convert into equal 3 bit ascii value
        if len(a) < 3:
            ascii_text = '0' * (3 - len(a)) + a
        else:
            ascii_text = a
        ascii_value.append(ascii_text)
    return ascii_value


def convert_to_binary(ascii_value):
    binary_values = []

    # convert into single string
    ascii = ''
    for i in ascii_value:
        ascii = ascii + ' ' + i

    print(ascii)
    # convert into binary format
    for digit in ascii:
        binary_values.append(bin(ord(digit))[2:].zfill(8))

    return binary_values


def text_input():
    string = input("Enter the plain text")
    return string.strip()


def String_Split(binary):
    mid = len(binary) // 2
    string1 = binary[:mid]
    string2 = binary[mid:]
    return (string1, string2)


def XOR_operation(message, key):

    len_message = len(message)
    encoded = []

    for i in range(0, len_message):
        a = i % len(key)
        encoded.append(int(message[i]) ^ int(key[a]))

    return encoded


def main():
    print('Welcome to the encryption part')
    string = text_input()

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

    with open("data.csv", "w") as csvfile:
        send_file = csv.writer(csvfile)
        send_file.writerow(encrypted_message)


if __name__ == '__main__':
    print("my name is saurav")
    main()
