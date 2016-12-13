import numpy as np

class NeuronLayer:
    def __init__(self, nodes, inputs_per_node):
        self.weights = 2 * np.random.random((inputs_per_node, nodes)) - 1

class TwoLayerNN:
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    def sigmoid(self, z, deriv=False):
        if deriv is True:
            return z * (1 - z)
        else:
            return 1/(1 + np.exp(-z))

    def train(self, X, y, n_iter=60000):
        for iter in range(n_iter):
            #cele 2 outputuri, cel de la layer1 la layer 2 si cel de la layer 2, final
            y_layer1, y_caciulita = self.think(X)
            error_layer2 = y - y_caciulita
            delta_layer2 = error_layer2 * self.sigmoid(y_caciulita, deriv=True)
            error_layer1 = np.dot(delta_layer2, self.layer2.weights.T)
            delta_layer1 = error_layer1 * self.sigmoid(y_layer1, deriv=True)
            self.layer1.weights += np.dot(X.T, delta_layer1)
            self.layer2.weights += np.dot(y_layer1.T, delta_layer2)

    def think(self, X):
        layer1_out = self.sigmoid(np.dot(X, self.layer1.weights))
        layer2_out = self.sigmoid(np.dot(layer1_out, self.layer2.weights))
        return layer1_out, layer2_out

    def print_weights(self):
        print("Layer 1 weights")
        print(self.layer1.weights)
        print("Layer 2 weights")
        print(self.layer2.weights)

if __name__ == '__main__':
    np.random.seed(1)
    neuron1 = NeuronLayer(4, 3)
    neuron2 = NeuronLayer(1, 4)
    x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    Y = np.array([[0, 1, 1, 1, 1, 0, 0]]).T
    neural_network = TwoLayerNN(neuron1, neuron2)
    neural_network.print_weights()
    neural_network.train(x, Y)
    neural_network.print_weights()
    y_hidden, y_estimate = neural_network.think(np.array([1, 1, 0]))
    print(y_estimate)