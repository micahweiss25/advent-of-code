from math import e

class NeuralNetwork:
    def __init__(self):
        pass
        self.layers = []
        self.activations = []

        #TODO: store layers, weights, and biases

    def __str__(self):
        str = ""
        for num, i in enumerate(self.layers):
            str += f"Layer {num}:\n" + f"Biases:\n{i.biases}\n"
            str += f"Weights:\n"
            for tmp in i.weights:
                str += f"{tmp}\n"
            #str += "activations"
        for i in self.activations:
            str += "Activation:\n"
            str += f"{i}\n"
        return str

    def addLayer(self, activation, nodes, input_size):
        self.layers.append(Layer(
            activation,
            nodes,
            input_size))
             
    def run(self, dataset):
        for data in dataset:
            activation = [i for i in data]
            self.activations.append(activation)
            for layer in self.layers:
                activation = layer.run(activation)
                self.activations.append(activation)


class Layer:
    def __init__(self, activation, nodes, input_size):
        self.activation = activation
        self.nodes = nodes
        self.biases = [0 for i in range(nodes)]
        self.input_size = input_size
        self.weights = [[0 for i in range(nodes)] for n in range(input_size)]
        
    def run(self, activations):
        '''the number of activations is equal to 
        th input_size'''
        new_activations = []
        '''new_activations = self.weights matrix multiplication activations'''
        for num in range(len(activations)):
            # multiple activations by the weight matrix
            var = [weight * activations[num] for weight in self.weights[num]]
            # sum the product 
            var = sum(var)
            # add the bias
            var += self.biases[num]
            # activation
            new_activations.append(sigmoid(var))
        return new_activations


        
def sum(list):
    tmp = 0
    for i in list:
        tmp += i
    return tmp

def sigmoid(x):
    (e ** x)
