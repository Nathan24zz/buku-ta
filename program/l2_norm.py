import numpy as np

def L2_normalization(self, input_test):
    for k in range(0, 6):
        nominator = input_test[:, k]
        denominator = np.linalg.norm(input_test[:, k])

        if denominator == 0:
            input_test[:, k] = [[0, 0]]
        else:
            input_test[:, k] = nominator / denominator
    return input_test

input = # array with shape (1,6,2)
L2_normalization(input)