from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if arr:
        seq = arr.copy()
        left_lim, right_lim = 0, len(seq) - 1

        while left_lim <= right_lim:
            middle = left_lim // 2 + right_lim // 2

            if seq[middle] == elem:
                while seq[middle - 1] == elem:
                    middle -= 1
                return middle
            else:
                if seq[middle] < elem:
                    left_lim = middle + 1
                else:
                    right_lim = middle - 1

    return None


if __name__ == '__main__':
    arr = [-1, 1, 1, 1, 2]
    print(binary_search(20, arr))
