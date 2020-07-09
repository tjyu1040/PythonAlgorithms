"""Module containing core computations in number theory."""
__all__ = ['gcd', 'lcm']

from functools import reduce

import numpy as np


def gcd(*integers: int) -> int:
    """
    Compute the greatest common divisor (GCD) of integers.

    The GCD is the largest positive integer that divides each of the integers.

    :param integers: Iterable of integers.
    :return: The largest positive integer that divides all the given integers.

    :Example:
    >>> gcd(0, 0)
    0
    >>> gcd(5, 5)
    5
    >>> gcd(0, 5)
    5
    >>> gcd(-5, 0)
    5
    >>> gcd(-3, 9)
    3
    >>> gcd(-27, -6)
    3
    >>> gcd(3, 5)
    1
    """
    if not integers:
        raise ValueError('integers must not be empty')

    if not is_integer(*integers):
        raise TypeError(f'invalid integer types found: {integers!r}')

    def _gcd(a: int, b: int) -> int:
        a, b = abs(a), abs(b)
        if a == 0 or b == 0 or a == b:
            return max(a, b)
        while b > 0:
            a, b = b, a % b
        return a

    return reduce(_gcd, integers)


def lcm(*integers: int) -> int:
    """
    Compute the least common multiple (LCM) of integers.

    The LCM is the smallest positive integer that is divisible by each of the integers.

    :param integers: Iterable of integers.
    :return: The smallest positive integer that is divisible by all the given integers.

    :Example:
    >>> lcm(1, 1)
    1
    >>> lcm(0, 5)
    0
    >>> lcm(5, 5)
    5
    >>> lcm(3, 5)
    15
    >>> lcm(10, 20)
    20
    >>> lcm(-10, 20)
    20
    """
    if not integers:
        raise ValueError('integers must not be empty')

    if not is_integer(*integers):
        raise TypeError(f'invalid integer types found: {integers!r}')

    def _lcd(a: int, b: int) -> int:
        if a == 0 and b == 0:
            raise RuntimeError('lcm(0, 0) is undefined')
        return abs(a * b) // gcd(a, b)

    return reduce(_lcd, integers)


def is_integer(*integers: int) -> bool:
    return all([isinstance(i, (int, np.integer)) for i in integers])
