from random import random
from math import exp
from text_encryption import Crossover, mutation, String_Split


def XOR_operation(encrypted_one, key1):
    len_message = len(encrypted_one)
    decoded = ''

    for i in range(0, len_message):
        a = i % len(key1)
        decoded += str(int(encrypted_one[i]) ^ int(key1[a]))

    return decoded


def convert_to_eight(data):
    dataset = []
    i = 0
    while i <= len(data):
        data1 = data[i:i + 8]
        dataset.append(data1)
        i = i + 8

    return dataset[:-1]


def binary_array(data):
    mutate = mutation(data)
    string1, string2 = String_Split(mutate)

    cross = Crossover(string1, string2)
    # mutate = mutation(cross)
    print('values after mutation')
    # print(mutate)
    print(cross)
    print(len(cross))
    print(".....")

    binary_value = []
    for i in cross:
        value = int(i, 2)
        binary_value.append(value)

    # print(binary_value)
    return binary_value
    # second conversion to the ascii
    # ascii_array=[]
    # for item in binary_value:
    #     char = chr(item)
    #     ascii_array.append(char)
    #
    # print(".....")
    # print(ascii_array)


def setnetwork(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))


def feedforward(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# Calculate the derivative of an neuron output
def derivative(output):
    return output * (1.0 - output)


# back propagates the error
def backpropogation(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * derivative(neuron['output'])


# Update network weights according to  error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += l_rate * neuron['delta']


def train_network(network, train_data, learn_rate, epoch_rate, n_outputs):
    error_sum = -1
    print('training the data')

    for row in train_data:
        outputs = feedforward(network, row)
        expected = [0 for i in range(255)]
        #print(row[-1])
        expected[row[-1]] = 1
        error_sum += sum([(expected[i]-outputs[i])**2/(255*2*10) for i in range(len(expected))])
        backpropogation(network, expected)
        update_weights(network, row, learn_rate)
        #print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

        #print(strt)
        if error_sum<=0.04:
            return error_sum
    return error_sum


def convert_to_list(data, cipher):
    datasets = []
    for i in range(0, len(data)):
        a = list(data[i])
        datasets.append(a)

    for i in range(len(datasets)):
        datasets[i] = [int(x, 2) for x in datasets[i]]
        datasets[i].append(cipher[i])
    # datasets = np.array(datasets).reshape(-1,2).tolist()
    return datasets


def find_key(message):
    length = int(len(message)/2)
    key = message[length-66:length+62]
    print(len(key))

    code = message[length+62:length+66]
    print(code)

    encrypted_message = message[:length-66]+message[length+66:]
    return encrypted_message,key,code

