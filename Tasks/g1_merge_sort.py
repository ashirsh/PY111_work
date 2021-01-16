from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def merge(left_part, right_part):
        result = []
        while left_part or right_part:
            if not left_part:
                result.extend(right_part)
                right_part.clear()
            elif not right_part:
                result.extend(left_part)
                left_part.clear()

            elif left_part[0] <= right_part[0]:
                result.append(left_part.pop(0))
            else:
                result.append(right_part.pop(0))
        return result

    if len(container) == 1:
        return container
    else:
        middle_index = len(container) // 2
    return merge(sort(container[:middle_index]), sort(container[middle_index:]))


if __name__ == '__main__':
    lst = [1, 3, 2, 5, 8, 7, 4, 6, 9, 0]
    print(sort(lst))
