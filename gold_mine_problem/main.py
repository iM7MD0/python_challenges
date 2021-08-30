import numpy as np


def start_function(matrix):
    global x
    for i in matrix[:, 8]:
        if i > x:
            x = i
            print(i)


def find_best_way():
    pass


if __name__ == '__main__':
    random_matrix = np.random.randint(100, size=(9, 9))
    print(random_matrix)
    print(start_function(random_matrix))
