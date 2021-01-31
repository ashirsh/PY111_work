def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    results = {(0, 0): 1}
    for i in range(3, sum(point)+1):
        coord = tuple((i-j, j) for j in range(i+1) if (i-j < shape[0] and j < shape[1]))
        for comb in coord:
            incomes = ((comb[0]-2, comb[1]-1), (comb[0]-2, comb[1]+1), (comb[0]+1, comb[1]-2), (comb[0]-1, comb[1]-2))
            for item in incomes:
                if item in results.keys():
                    results[comb] = results.get(comb, 0) + results[item]

    return results[point]


if __name__ == '__main__':
    print(calculate_paths((5, 5), (4, 4)))
    print(calculate_paths((8, 8), (7, 7)))
    print(calculate_paths((9, 9), (8, 8)))
    print(calculate_paths((17, 12), (16, 9)))
    print(calculate_paths((12, 10), (11, 9)))
