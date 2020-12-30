def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    fib = [0, 1]
    if n < 0:
        raise ValueError
    if n > 1:
        for i in range(1, n):
            item = fib[i-1] + fib[i]
            fib.append(item)
    return fib[n]


if __name__ == '__main__':
    print(fib_recursive(7))
    print(fib_iterative(7))
