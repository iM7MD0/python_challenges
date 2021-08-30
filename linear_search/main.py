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
    middle_element = int(len(py_list) / 2)
    print("middle_element", middle_element)
    print("py_list[:middle_element]", py_list[:middle_element])
    final_element = py_list[-1]
    if first_element <= val < middle_element:
        for i in py_list[:middle_element]:
            if i == val:
                return val
    elif middle_element <= val <= final_element:
        for j in py_list[middle_element:]:
            if j == val:
                return val
    return None


if __name__ == '__main__':
    
    #search_list = np.random.normal(52, 30, 100).astype(int)
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 111, 121, 131, 141, 151, 161, 171, 181]

    sorted_search_list = search_list.copy()
    sorted_search_list.sort()

    print(search_list)
    tm1 = time.time()
    print(search(search_list, 450))
    tm2 = time.time()
    print("normal search timing =", tm2 - tm1)
    print(sorted_search_list)

    tp1 = time.time()

    print(search_sorted(sorted_search_list, 151))

    tp2 = time.time()
    print("sorted timing =", tp2 - tp1)
