import numpy as np


def print_matrix(name, shape, values):
    print("Matrix {name}({shape}) :\n{values}\n".format(name=name, shape=shape, values=values))
    np.savetxt("{name}.csv".format(name=name), values, delimiter=",")


def method1(h, x):
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
    h = np.matrix([
        [2, 4, 3, 0, 0, 0, 0, 4],
        [2, 3, 3, 4, 3, 2, 4, 3],
        [0, 0, 5, 6, 0, 1, 0, 5],
        [0, 5, 3, 3, 3, 3, 4, 0],
        [0, 4, 2, 4, 5, 4, 6, 0],
        [0, 3, 4, 0, 0, 5, 6, 0],
        [3, 0, 4, 0, 5, 0, 6, 0],
        [4, 0, 3, 0, 6, 0, 7, 0]])

    x = np.matrix([
        [3, 3, 0, 4, 4, 0, 3, 3],
        [0, 0, 2, 3, 3, 2, 0, 0],
        [0, 0, 5, 4, 4, 5, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0],
        [0, 3, 4, 5, 5, 4, 3, 0],
        [0, 0, 3, 4, 4, 3, 0, 0],
        [0, 0, 0, 3, 3, 0, 0, 0],
        [0, 4, 3, 2, 0, 5, 4, 2]])

    print_matrix("H", h.shape, h)
    print_matrix("X", x.shape, x)
    print("=============================== Method 1 ===============================")
    y = method1(h, x)
    print_matrix("Y", y.shape, y)
    print("=============================== Method 2 ===============================")
    y = method2(h, x)
    print_matrix("Y", y.shape, y)
