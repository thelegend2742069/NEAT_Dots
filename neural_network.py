import random
from math import exp

def activation(input):
    # print(input)
    output = 1/(1+exp(-input)) - 0.5
    # print(output)
    return output


class Layer:
    def __init__(self, in_nodes:list, out_nodes:list, weights:list = [], biases:list = []) -> None:
        self.in_nodes = in_nodes
        self.out_nodes = out_nodes

        # print("creating weights")
        if weights == []:
            self.weights = [[random.uniform(-5, 5) for _ in range(out_nodes)] for _ in range(in_nodes)]
        else: self.weights = weights
        
        if biases == []:
            self.biases = [random.uniform(-1, 1) for _ in range(out_nodes)]
        else: self.biases = biases

        print(f'{self.weights=}, {self.biases=}')

    
    def calculate_output(self, inputs:list) -> list:
        output = [self.biases[i] for i in range(self.out_nodes)]

        for j in range(self.out_nodes):
            for i in range(self.in_nodes):
                # print(f'{j=}, {inputs[i]=}, {self.weights[i][j]=}')
                output[j] += inputs[i] * self.weights[i][j]
        
        output = [activation(output[j]) for j in range(self.out_nodes)]
        print(output)
        return output



class NeuralNetwork:
    def __init__(self, nodes_per_layer:list) -> None:
        # print("creating layer")
        self.layers = [Layer(nodes_per_layer[i], nodes_per_layer[i+1]) for i in range(len(nodes_per_layer)-1)]

    
    def calculate_output(self, inputs:list) -> list:
        for i in range(len(self.layers)):
            inputs = self.layers[i].calculate_output(inputs)
        
        return inputs