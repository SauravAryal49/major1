import random
import math
import sympy
from key_generation import Crossover, mutation


def convert_to_ascii(Strings):
    ascii_value = []
    for c in Strings:
        a = str(ord(c))
        # convert into equal 3 bit ascii value
        if len(a) < 3:
            ascii_text = '0'*(3-len(a))+a
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

    # convert into binary format
    for digit in ascii:
        binary_values.append(bin(ord(digit))[2:].zfill(8))

    return binary_values


def text_input():
    string = input("Enter the plain text")
    return string.strip()


# def String_Split(binary):


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
    # string1, string2 = String_Split(binary_values)


if __name__ == '__main__':
    print("my name is saurav")
    main()
