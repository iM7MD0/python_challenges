import numpy as np
import time


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

    val = np.random.normal(50, 30, 50000).astype(int)

    tm1 = time.time()
    list_min(val)
    tm2 = time.time()
    print("list_min() timing =", tm2 - tm1)

    tp1 = time.time()
    min(val)
    tp2 = time.time()
    print("python min() timing =", tp2 - tp1)
    print("min() ratio =", (tm2 - tm1) / (tp2 - tp1) * 100)

    t1 = time.time()
    list_max(val)
    t2 = time.time()
    print("list_max() timing =", t2 - t1)

    t1 = time.time()
    max(val)
    t2 = time.time()
    print("python max() timing =", t2 - t1)
    print("min() ratio =", (tm2 - tm1) / (tp2 - tp1) * 100)

    tm1 = time.time()
    list_sort(val)
    tm2 = time.time()
    print("list_sort() timing =", tm2 - tm1)

    tp1 = time.time()
    val.sort()
    tp2 = time.time()
    print("python sort() timing =", tp2 - tp1)
    print("min() ratio =", (tm2 - tm1) / (tp2 - tp1) * 100)
