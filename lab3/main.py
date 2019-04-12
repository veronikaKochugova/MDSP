import numpy as np


def print_matrix(name, shape, values):
    print("Matrix {name}{shape} :\n{values}\n".format(name=name, shape=shape, values=values))
    # np.savetxt("{name}.csv".format(name=name), values, delimiter=",")


def method1(y, filter):
    x_row = x.shape[0]
    x_col = x.shape[1]
    h_row = h.shape[0]
    h_col = h.shape[1]
    y_row = (h_row + x_row - 1)
    y_col = (h_col + x_row - 1)
    y = np.zeros((y_row, y_col))
    for i in range(y_row):
        for j in range(y_col):
            for k1 in range(h_row):
                for k2 in range(h_col):
                    if (i - k1 >= 0) & (i - k1 < x_row) & (j - k2 < x_col) & (j - k2 >= 0):
                        y[i, j] += h[k1, k2] * x[i - k1, j - k2]
    return y


def method2(h, x):
    x_row = x.shape[0]
    x_col = x.shape[1]
    h_row = h.shape[0]
    h_col = h.shape[1]
    y_row = (h_row + x_row - 1)
    y_col = (h_col + x_row - 1)
    y = np.zeros((y_row, y_col))
    count = 0
    for k1 in range(x_row):
        for k2 in range(x_col):
            temp = np.zeros((y_row, y_col))
            for m1 in range(h_row):
                for m2 in range(h_col):
                    temp[m1 + k1, m2 + k2] = h[m1, m2] * x[k1, k2]
            count += 1
            print_matrix("TEMP" + str(count), temp.shape, temp)
            y += temp
    return y


if __name__ == '__main__':

    # read result matrix from lab 2
    y = np.genfromtxt('../lab2/Y.csv', delimiter=',')
    print_matrix("Y", y.shape, y)
    # add noise
    y[6,5] = 400
    y[8,9] = 400
    print_matrix("Y with noise", y.shape, y)
    filter = np.matrix([[3,2,1],[2,4,2],[1,2,3]])
    print("=============================== Method 1 ===============================")
    y = method1(y, filter)
    # print_matrix("Y", y.shape, y)
    print("=============================== Method 2 ===============================")
    # y = method2(h, x)
    # print_matrix("Y", y.shape, y)
