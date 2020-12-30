"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    if arr:
        min_ = 0
        for i in range(len(arr)):
            if arr[i] < arr[min_]:
                min_ = i
        return min_
    return -1


if __name__ == '__main__':
    print(min_search([0, 1, -1, 1, -1]))
