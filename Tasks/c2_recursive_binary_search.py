from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    seq = arr.copy()
    left_lim, right_lim = 0, len(seq) - 1

    def recursive_bs(left, right):
        if left <= right:
            middle = left // 2 + right // 2
            if seq[middle] == elem:
                while seq[middle-1] == elem and middle > 0:
                    middle -= 1
                return middle
            elif seq[middle] > elem:
                return recursive_bs(left, middle-1)
            else:
                return recursive_bs(middle+1, right)
        return None

    return recursive_bs(left_lim, right_lim)


if __name__ == '__main__':
    lst = [-1, 0, 1, 1, 2, 2, 2, 2, 3]
    print(binary_search(1, lst))
