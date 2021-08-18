import numpy as np


def list_max(in_list):
    max = 0
    for i in in_list:
        if i > max:
            max = i
            # print(max)
            # print(i)
    return max


def list_min(in_list):
    min = 0
    for i in in_list:
        if i < min:
            min = i
            # print(max)
            # print(i)
    return min


if __name__ == "__main__":
    # print("hello!")

    val = np.random.normal(15, 7, 1000).astype(int)

    print(list_min(val))

    print(list_max(val))
