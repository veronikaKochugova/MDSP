import numpy as np


def print_matrix(name, shape, values):
    print("Matrix {name}{shape} :\n{values}\n".format(name=name, shape=shape, values=values))
    np.savetxt("{name}.csv".format(name=name), values, delimiter=",")


def method1(y, filter):
    row = y.shape[0]
    col = y.shape[1]
    window = 3
    signal = y
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            sg = 0
            for k1 in range(window):
                for k2 in range(window):
                    sg += filter[k1, k2] * y[i - 1 + k1, j - 1 + k2]
            signal[i, j] = sg
    return y


def method2(y, m):  # statistic filter(nu=m * sigma)
    row = y.shape[0]
    col = y.shape[1]
    window = 3
    signal = y
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            sum1 = 0
            sum2 = 0
            for k1 in range(window):
                for k2 in range(window):
                    sum1 += y[i - 1 + k1, j - 1 + k2]
            G = sum1 / pow(window, 2)
            for k1 in range(window):
                for k2 in range(window):
                    sum2 += pow(y[i - 1 + k1, j - 1 + k2] - G, 2)
            D = sum2 / (pow(window, 2) - 1)
            nu = m * pow(D, 0.5)
            signal[i, j] = y[i, j] if (y[i, j] - G) < nu else G
    return y


if __name__ == '__main__':
    # read result matrix from lab 2
    y = np.genfromtxt('../lab2/Y.csv', delimiter=',')
    print_matrix("Y", y.shape, y)
    # add noise
    y[6, 5] = 400
    y[8, 9] = 400
    print_matrix("Y with noise", y.shape, y)
    filter = (1 / 19) * np.matrix([[3, 2, 1], [2, 4, 2], [1, 2, 3]])
    print_matrix("Filter", filter.shape, filter)
    print("=============================== Method 1 ===============================")
    y1 = method1(y.copy(), filter)
    delta = abs(y - y1)
    print_matrix("Y1", y1.shape, y1)
    print_matrix("Delta1", delta.shape, delta)
    print("=============================== Method 2 ===============================")
    y2 = method2(y.copy(), 1.26)
    delta = abs(y - y1)
    print_matrix("Y2", y2.shape, y2)
    print_matrix("Delta2", delta.shape, delta)
