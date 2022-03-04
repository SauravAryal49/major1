
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


def bind_key_to_message(message, code):
    file = open("key.txt", 'r')
    key = file.read()
    print(type(key))

    data = ''.join(str(e) for e in message)
    print(type(data))
    length = int(len(data)/2)
    print(length)

    actual_data = data[:length]+key+code+data[length:]
    print(len(actual_data))
    print(code)
    list_data = [int(a) for a in actual_data]


    return list_data






