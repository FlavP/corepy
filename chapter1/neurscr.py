import numpy as np

class NeuralNetwork():
    def __init__(self):
        self.inputLayers = 2
        self.hiddenLayers = 3
        self.outputLayers = 1

    def sigmoid(self, z, deriv=False):
        if deriv is True:
            return np.exp(-z)/((1 + np.exp(-z))**2)
        return 1/(1 + np.exp(-z))

    def forward(self, X):
        np.random.seed(1)
        self.W1 = 2 * np.random.random((self.inputLayers, self.hiddenLayers)) - 1
        self.W2 = 2 * np.random.random((self.hiddenLayers, self.outputLayers)) - 1
        self.z2 = np.dot(X * self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        Y_creasta = self.sigmoid(self.z3)
        return Y_creasta

    def backProp(self, X, y):
        self.y_creasta = self.forward(X)
        #In delta3 inmultesti diferenta dintre y si y_creasta cu sigmoida derivata a lui z3, care da sensul
        #functiei, deci semnul
        delta3 = np.multiply(-(y - self.y_creasta), self.sigmoid(self.z3, deriv=True))
        #derivata celei de a 2-a greutati (weight) in raport cu J, la gradient descent
        dJdW2 = np.dot(self.a2.T * delta3)
        #Se ia in sens invers, la primul backprop ai output inmultit cu eroarea, acum ai dot product
        #dintre delta3, care se propaga si weight transpose, pentru a modifica weights1 si inmultit cu
        # sig derivat de z2
        delta2 = np.dot(delta3, self.W2.T) * self.sigmoid(self.z2, deriv=True)
        dJdW1 = np.dot(X.T, delta2)
        return dJdW1, dJdW2


