import json
from activation_function import *

with open("format_model.json") as f:
    json_content = json.load(f)
    # print(json_content)

    # input layer
    input_amount = json_content["input_amount"]
    x_input_layer = json_content["input_array"]

    # hidden layers
    hidden_layers = json_content["hidden_layers"]
    amount_hidden_layers = hidden_layers["amount"]
    layers = hidden_layers["layers"]  

    # output layer
    output_layer = json_content["output_layer"]

def calculateActivation(input, activation_type=None, input_array=None) -> float:
    if(activation_type == 'Linear'):
        return linear(input)
    elif(activation_type == 'ReLU'):
        return relu(input)
    elif(activation_type == 'Sigmoid'):
        return sigmoid(input)
    elif(activation_type == 'Softmax'):
        return softmax(input, input_array)
    
    return input

def calculateNeuronOutputPreActivation(input_array, neuron_weight) -> float:
    output = 1 * neuron_weight[0]
    
    for i in range(len(input_array)):
        output += input_array[i] * neuron_weight[i+1]
    
    return output

def calculateLayerOutput(layer, input_array):
    activation_type = layer["activation_type"]
    layer_neurons = layer["neurons"]
    neuron_amount = layer["neuron_amount"]
    output_array = []

    # temp = 0
    if(activation_type == 'Linear'):
        for i in range(neuron_amount):
            neuron_weight = layer_neurons[i]["weight"]
            temp = calculateNeuronOutputPreActivation(input_array, neuron_weight)
            temp = linear(temp)
            output_array.append(temp)
    elif(activation_type == 'ReLU'):
        for i in range(neuron_amount):
            neuron_weight = layer_neurons[i]["weight"]
            temp = calculateNeuronOutputPreActivation(input_array, neuron_weight)
            temp = relu(temp)
            output_array.append(temp)
    elif(activation_type == 'Sigmoid'):
        for i in range(neuron_amount):
            neuron_weight = layer_neurons[i]["weight"]
            temp = calculateNeuronOutputPreActivation(input_array, neuron_weight)
            # print("temp1: ", temp)
            temp = sigmoid(temp)
            # print("temp2: ", temp)
            output_array.append(temp)
    elif(activation_type == 'Softmax'):
        for i in range(neuron_amount):
            neuron_weight = layer_neurons[i]["weight"]
            temp = calculateNeuronOutputPreActivation(input_array, neuron_weight)
            temp = softmax(temp, input_array)
            output_array.append(temp)

    print("Layer output: ", output_array)
    return output_array

def calculateOutputLayerOutput(output_layer, input_array) -> float:
    neuron_weight = output_layer["weight"]
    activation_type = output_layer["activation_type"]
    
    temp = calculateNeuronOutputPreActivation(input_array, neuron_weight)
    # print("temp1: ", temp)
    temp = calculateActivation(temp, activation_type, input_array)
    # print("temp2: ", temp)
    
    return temp

    
def predict(x_input_layer, hidden_layers, output_layer):
    
    # output layer
    output_array = calculateLayerOutput(hidden_layers[0], x_input_layer)
    
    for i in range(1, len(hidden_layers)):
        output_array = calculateLayerOutput(hidden_layers[i], output_array)

    output = calculateOutputLayerOutput(output_layer, output_array)
    
    return output
    
        
def show_model(json_content):
    # input layer
    input_amount = json_content["input_amount"]
    x_input_layer = json_content["input_array"]

    # hidden layers
    hidden_layers = json_content["hidden_layers"]
    amount_hidden_layers = hidden_layers["amount"]
    layers = hidden_layers["layers"]  

    # output layer
    output_layer = json_content["output_layer"]

    print("Input Layer:")
    print("     Input Amount:", input_amount)
    print("     Neurons:")
    for i, neuron in enumerate(x_input_layer):
        print("         Neuron", str(i)+":",  neuron)
    for i, hidden_layer in enumerate(layers):
        print("Hidden Layer ", str(i)+ ":")
        print("     Activation Type:", hidden_layer["activation_type"])
        print("     Neuron:")
        neurons = hidden_layer["neurons"]
        for j, neuron in enumerate(neurons):
            print("         Neuron", str(j)+":")
            print("         Bobot:", neuron["weight"])
    print("Output Layer:")
    print("     Activation Type:", output_layer["activation_type"])
    print("     Bobot:", output_layer["weight"])

print("Hasil prediksi: ", predict(x_input_layer, layers, output_layer))
show_model(json_content)