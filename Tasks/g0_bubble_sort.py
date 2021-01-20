from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input _list with bubble sort

    :param container: _list of elements to be sorted
    :return: _list sorted in ascending order
    """

    for i in range(len(container)-1):
        for j in range(len(container)-i-1):
            if container[j+1] < container[j]:
                container[j+1], container[j] = container[j], container[j+1]

    return container


if __name__ == '__main__':
    lst = [1, 3, 4, 5, 2, 8, 5, 0, 9, 6, 7, 0]
    print(sort(lst))
