"""
Taylor series
"""
from typing import Union
from math import factorial

Delta = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def elem(n):
        return x ** n / factorial(n)

    sum_, count_ = 0, 0
    while elem(count_) > Delta:
        sum_ += elem(count_)
        count_ += 1
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    def elem(n):
        return -1 ** n * (x ** (2 * n + 1) / factorial(2 * n + 1))

    sum_, count_ = 0, 0
    while elem(count_) > Delta:
        sum_ += elem(count_)
        count_ += 1
    return sum_
