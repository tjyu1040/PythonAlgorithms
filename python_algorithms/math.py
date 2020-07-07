"""Module containing mathematics."""


def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers.

    The GCD is the largest positive integer that divides each of the integers.

    :param a: An integer.
    :param b: An integer.
    :return: The largest positive integer that divides both `a` and `b`.

    :Example:
    >>> gcd(0, 0)
    0
    >>> gcd(5, 5)
    5
    >>> gcd(0, 5)
    5
    >>> gcd(0, -5)
    5
    >>> gcd(-3, 9)
    3
    >>> gcd(-27, -6)
    3
    >>> gcd(3, 5)
    1
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f'a and b must be non-negative numbers, got {a} and {b}')
    a, b = abs(a), abs(b)
    if a == 0 or b == 0 or a == b:
        return max(a, b)
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple (LCM) of two integers.

    The LCM is the smallest positive integer that is divisible by each of the integers.

    :param a: An integer.
    :param b: An integer.
    :return: The smallest positive integer that is divisible by both `a` and `b`.

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
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f'a and b must be non-negative numbers, got {a} and {b}')
    if a == 0 and b == 0:
        raise RuntimeError('lcm(0, 0) is undefined since the only multiple of 0 is 0.')
    return abs(a * b) // gcd(a, b)
