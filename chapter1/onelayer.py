import numpy as np

class OneLayerNN():
    def __init__(self):
        np.random.seed(1)
        self.weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, z, deriv=False):
        if deriv is True:
            return np.exp(-z)/((1 + np.exp(-z))**2)
        else:
            return 1/(1 + np.exp(-z))

    def train(self, X, y, n_iter=10000):
        for iter in range(n_iter):
            y_caciula = self.think(X)
            error = y - y_caciula
            delta_error = error * self.sigmoid(y, deriv=True)
            self.weights += np.dot(X.T, delta_error)

    def think(self, X):
        #weighted result, or a, produsul x * weights, care mai apoi vedem daca trece sau nu pragul
        a_out = np.dot(X, self.weights)
        return self.sigmoid(a_out)

if __name__ == '__main__':
    neural_network = OneLayerNN()
    X = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    y = np.array([[0, 1, 1, 0]]).T
    test_X = np.array([[1, 0, 0]])
    #print(neural_network.weights)
    neural_network.train(X, y)
    #print(neural_network.weights)
    print(neural_network.think(test_X))
