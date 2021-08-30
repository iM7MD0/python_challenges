import numpy as np
import time


def search(in_list, val):
    for i in in_list:
        if i == val:
            return val
    return None


def search_sorted(in_list, val):
    py_list = list(in_list.copy())

    middle_element = int(len(py_list) / 2)
    print("middle_element", middle_element)
    print("py_list[:middle_element]", py_list[:middle_element])
    print("py_list[middle_element:]", py_list[middle_element:])
    if val <= middle_element:
        for i in py_list[:middle_element]:
            print(i)
            if i == val:
                return val
    else:
        for j in py_list[middle_element:]:
            print(j)
            if j == val:
                return val
    return None


def binary_search(in_list, val):
    py_list = list(in_list.copy())
    first_element = 0
    last_element = int(len(py_list) - 1)
    found = False
    print(first_element, last_element)

    while first_element <= last_element and not found:
        middle_element = (first_element + last_element) // 2
        print(first_element, middle_element, last_element)
        if py_list[middle_element] == val:
            found = True
        else:
            if val < py_list[middle_element]:
                last_element = middle_element - 1
            else:
                first_element = middle_element + 1

    return found


if __name__ == '__main__':
    # search_list = np.random.normal(50, 30, 100).astype(int)
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 111, 121, 131, 141, 151, 161, 171, 181]

    sorted_search_list = search_list.copy()
    sorted_search_list.sort()

    print(sorted_search_list)
    # tm1 = time.time()
    # print(search(search_list, 450))
    # tm2 = time.time()
    # print("normal search timing =", tm2 - tm1)
    # print(sorted_search_list)
    #
    # tp1 = time.time()
    #
    # print(search_sorted(sorted_search_list, 550))
    #
    # tp2 = time.time()
    # print("sorted timing =", tp2 - tp1)
    print(binary_search(sorted_search_list, ))
