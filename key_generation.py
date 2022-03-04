import random
import math
import sympy
import string


def convert_to_ascii(Strings):
    ascii_value = []
    for c in Strings:
        a = str(ord(c))
        ascii_value.append(a)
    return ascii_value


def convert_to_binary(Strings):
    binary_value = []

    for digit in Strings:
        if type(digit) == int:
            binary_value.append(bin(digit)[2:].zfill(8))
        else:
            binary_value.append(bin(ord(digit))[2:].zfill(8))

    return binary_value


def Crossover(String1, String2):
    cross = []
    cross1 = []
    cross2 = []
    temp = String1
    for i in range(len(String1)):
        temp1 = String1[i][0:4] + String2[i][4:]
        temp2 = String2[i][0:4] + String1[i][4:]
        # print(temp1, temp2)
        cross1.append(temp1)
        cross2.append(temp2)
        # cross.append(temp1)
        # cross.append(temp2)

    cross = cross1+cross2
    return cross


def mutation(Strings):
    mutate = []
    for value in Strings:
        temp = value[0]
        temp1 = value[1:-1]
        temp2 = value[-1]

        if temp == "1":
            temp = "0"
        else:
            temp = "1"

        if temp2 == "1":
            temp2 = "0"

        else:
            temp2 = "1"

        temp_data = temp+temp1+temp2

        mutate.append(temp_data)
    return mutate


def calculate_shanon_entropy(Strings):
    print("calculation of the entropy")
    value = []
    for i in range(0, 16):
        random_value = random.choice(Strings)
        value.append(random_value)

    print(value)
    shanon_entropy = 0
    for c in value:
        print(c)
        print(value.count(c))
        prob = float(value.count(c))/len(value)
        print(prob)
        entropy_i = - prob*(1/math.log2(prob))
        shanon_entropy += entropy_i

    print(shanon_entropy)
    return shanon_entropy, value


def main():
    print("Welcome to the encryption part")
    characters = []
    prime = []
    for i in range(0, 16):
        a = sympy.randprime(0, 100)
        prime.append(a)
        b = random.choice(string.ascii_uppercase)
        characters.append(b)

    print("16 random characters")
    print(characters)
    ascii_characters = convert_to_ascii(characters)
    print("ascii value of characters")
    print(ascii_characters)
    print("16 random prime numbers")
    print(prime)

    binary_characters = convert_to_binary(characters)

    print(binary_characters)

    binary_prime = convert_to_binary(prime)
    print(binary_prime)
    i = 1
    while i:
        cross = Crossover(binary_prime, binary_characters)
        print("crossover values")
        print(cross)

        mutate = mutation(cross)
        print("mutated values")
        print(mutate)

        entropy_value, key_value = calculate_shanon_entropy(mutate)
        if entropy_value > 0.95:
            i = 0

    key = ''.join(key_value)
    print(key, len(key))

    file = open("key.txt", "w")
    file.write(key)
    file.close()





if __name__ == '__main__':
    main()
