from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    price = [float('inf')] * len(stairway)
    price[0] = stairway[0]
    price[1] = stairway[1]

    for i in range(2, len(stairway)):
        price[i] = min(price[i-2], price[i-1]) + stairway[i]

    return price[-1]


if __name__ == '__main__':
    test = [1, 0, 1, 1, 0, 2, 0, 1, 1, 2]
    print(stairway_path(test))
