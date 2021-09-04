import numpy as np


def start_function(matrix):
    path = []
    first_max = np.argmax(matrix[:, 0])
    path.append(first_max)

    for i in range(1, len(matrix[0])):
        current = path[i - 1]
        if current == 0:
            possible_vals = matrix[current: current + 2, i]
            new_move = np.argmax(possible_vals)
            path.append(current + new_move)

        elif current == len(matrix[:, 0]) - 1:
            possible_vals = matrix[current - 1: current + 1, i]
            new_move = np.argmax(possible_vals)
            path.append(current + new_move - 1)

        else:
            possible_vals = matrix[current - 1: current + 2, i]
            new_move = np.argmax(possible_vals)
            path.append(current + new_move - 1)

    return path

def find_best_way():
    pass


if __name__ == '__main__':
    random_matrix = np.random.randint(100, size=(9, 9))
    print(random_matrix)
    print(start_function(random_matrix))
