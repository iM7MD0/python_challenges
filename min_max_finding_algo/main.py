import numpy as np


def list_max(in_list):
    for i in in_list:
        for j in in_list[i]:
            print(i)


def list_min(in_list):
    pass


if __name__ == "__main__":
    print("hello!")

    val = np.random.normal(15, 7, 1000).astype(int)

    print(val)

    print(list_min(val))

    print(list_max(val))
