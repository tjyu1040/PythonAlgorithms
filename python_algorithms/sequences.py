"""Module containing algorithms involved with generating sequences."""
from typing import Iterator


def fibonacci_number(n: int) -> int:
    """
    Generate the n-th term of the `Fibonacci sequence <https://en.wikipedia.org/wiki/Fibonacci_number>`_.

    :param n: The n-th term to compute.
    :return: The n-th Fibonacci number.

    :Example:
    >>> fibonacci_number(0)
    0
    >>> fibonacci_number(1)
    1
    >>> fibonacci_number(2)
    1
    >>> fibonacci_number(3)
    2
    >>> fibonacci_number(10)
    55
    """
    if n < 0:
        raise ValueError(f'Nth term must be a non-negative integer number, got {n}')

    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b

    i = 2
    fib_value = a + b
    while i <= n:
        fib_value = a + b
        a = b
        b = fib_value
        i += 1

    return fib_value


def fibonacci_sequence(length: int) -> Iterator[int]:
    """
    Generate the `Fibonacci sequence <https://en.wikipedia.org/wiki/Fibonacci_number>`_.

    :param length: The length of the Fibonacci sequence to generate.
    :return: Iterator of the Fibonacci sequence.
    """
    if length < 0:
        raise ValueError(f'Length must be a non-negative number, got {length}')

    a, b = 0, 1
    if length >= 1:
        yield a
    if length >= 2:
        yield b

    for i in range(length - 2):
        fib_value = a + b
        yield fib_value
        a = b
        b = fib_value
