"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    res = 1
    denominator = 1
    numerator = 1

    for i in range(1, 10):
        numerator = numerator * x
        denominator = denominator * i

        res += numerator / denominator

    return res


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    res = x
    numerator = x
    denominator = 1
    coefficient_fctrl = 1

    for i in range(1, 10):
        numerator = numerator * (x ** 2)
        denominator = denominator * (coefficient_fctrl + 1) * (coefficient_fctrl + 2)
        coefficient_fctrl += 2
        res = res + (numerator / denominator) * (-1) ** i

    return res
