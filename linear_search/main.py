import numpy as np


def search(in_list, val):
    for i in in_list:
        if i == val:
            x = np.where(in_list == val)
            return x, val
    return None


def search_sorted(in_list, val):
    pass


if __name__ == '__main__':
    search_list = np.random.normal(50, 30, 100).astype(int)

    sorted_search_list = search_list.copy()
    sorted_search_list.sort()

    print(search_list)

    print(search(search_list, 44))

    print(sorted_search_list)
