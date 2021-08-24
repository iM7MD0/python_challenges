import numpy as np
import time


def search(in_list, val):
    for i in in_list:
        if i == val:
            return val
    return None


def search_sorted(in_list, val):
    py_list = list(in_list.copy())
    first_element = py_list[0]
    middle_element = py_list[int(len(py_list) / 2)]
    final_element = py_list[-1]
    for i in py_list:
        if first_element <= i < middle_element:
            if i == val:
                return val
        elif middle_element <= i <= final_element:
            if i == val:
                return val
    return None


if __name__ == '__main__':
    search_list = np.random.normal(5250, 300, 100000).astype(int)

    sorted_search_list = search_list.copy()
    sorted_search_list.sort()

    print(search_list)
    t1 = time.time()
    print(search_list, 44)
    t2 = time.time()
    print("normal search timing =", t2 - t1)
    print(sorted_search_list)

    tp1 = time.time()
    print(search_sorted(sorted_search_list, 4343))
    tp2 = time.time()
    print("sorted timing =", tp2 - tp1)
