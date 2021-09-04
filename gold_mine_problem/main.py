import numpy as np


def start_function(matrix):
    path = []
    first_max = np.argmax(matrix[:, 0])
    path.append(first_max)

    for i in range(1, len(matrix[0])):
        here = path[i - 1]
        if here == 0:
            values = matrix[here: here + 2, i]
            next_step = np.argmax(values)
            path.append(here + next_step)
        else:
            values = matrix[here - 1: here + 2, i]
            next_step = np.argmax(values)
            path.append(here + next_step - 1)
    return path


def find_best_way():
    pass


if __name__ == '__main__':
    random_matrix = np.random.randint(100, size=(9, 9))
    print(random_matrix)
    print(start_function(random_matrix))
