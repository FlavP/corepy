import numpy as np

def sig(X, deriv=False):
    if deriv is True:
        return np.exp(-X)/((1 + np.exp(-X))**2)
    return 1/(1 + np.exp(-X))

def train(X, y):
    np.random.seed(1)
    #print(len(X))
    weights_0 = 2 * np.random.random((len(X[0]), len(X))) - 1
    weights_1 = 2 * np.random.random((len(X), 1)) - 1
    #print(weights_0)
    for iter in range(60000):
        layer0 = X
        layer1 = sig(np.dot(layer0, weights_0))
        layer2 = sig(np.dot(layer1, weights_1))
        error_l2 = y - layer2
        delta_l2 = error_l2 * sig(layer2, deriv=True)
        error_l1 = delta_l2.dot(error_l2.T)
        delta_l1 = error_l1 * sig(layer1, deriv=True)
        weights_1 += layer1.T.dot(delta_l2)
        weights_0 += layer0.T.dot(delta_l1)
        if iter % 10000 == 0:
            print("Error: ", str(np.mean(np.abs(error_l2))))

    return layer2

#print(weights_1)


X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0,1,1,0]]).T

halm = train(X, y)
print(halm)
