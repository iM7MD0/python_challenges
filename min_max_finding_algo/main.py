import numpy as np
import time

sec = time.time()


def list_max(in_list):
    imax = in_list[0]
    for i in in_list:
        if i > imax:
            imax = i
            # print(max)
            # print(i)
    return imax


def list_min(in_list):
    imin = in_list[0]
    for i in in_list:
        if i < imin:
            imin = i
            # print(max)
            # print(i)
    return imin


def list_sort(in_list):
    in_list_sorted = []
    py_list = list(in_list.copy())

    for i in in_list:
        x = list_max(py_list)
        in_list_sorted.append(x)
        py_list.remove(x)
    return in_list_sorted

    return in_list_sorted


if __name__ == "__main__":
    # print("hello!")


    val = np.random.normal(50, 30, 100).astype(int)

    print(list_min(val), min(val))

    print(list_max(val), max(val))

    print(list_sort(val))
