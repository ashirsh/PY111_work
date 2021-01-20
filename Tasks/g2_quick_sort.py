from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input _list with quick sort

    :param container: _list of elements to be sorted
    :return: _list sorted in ascending order
    """

    def sort_rec(_list, first_index, last_index):

        if first_index >= last_index:
            return

        base = _list[random.randint(first_index, last_index)]
        i, j = first_index, last_index

        while i <= j:
            while _list[i] < base:
                i += 1
            while _list[j] > base:
                j -= 1

            if i <= j:
                _list[i], _list[j] = _list[j], _list[i]
                i, j = i + 1, j - 1
        sort_rec(_list, first_index, j)
        sort_rec(_list, i, last_index)

    left_index, right_index = 0, len(container)-1
    sort_rec(container, left_index, right_index)

    return container


if __name__ == '__main__':
    lst = [1, 3, 2, 5, 8, 7, 4, 6, 9, 0]
    print(lst)
    print(sort(lst))
