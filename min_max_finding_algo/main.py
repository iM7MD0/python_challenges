import numpy as np


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
	pass

if __name__ == "__main__":
    # print("hello!")

    val = np.random.normal(-100, 2, 1000).astype(int)

    print(list_min(val), min(val))

    print(list_max(val), max(val))
