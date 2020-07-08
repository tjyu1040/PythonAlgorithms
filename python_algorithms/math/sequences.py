"""Module containing algorithms involved with generating mathematical sequences."""
__all__ = [
    'fibonacci_number', 'fibonacci', 'collatz'
]

from typing import Iterator


def fibonacci_number(n: int) -> int:
    """
    Generate the n-th term number of the `Fibonacci sequence <https://en.wikipedia.org/wiki/Fibonacci_number>`_.

    :param n: The n-th Fibonacci term number to compute.
    :return: The n-th Fibonacci term number.

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
        raise ValueError(f'n must be a non-negative integer number: {n}')

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


def fibonacci(length: int) -> Iterator[int]:
    """
    Generate the `Fibonacci sequence <https://en.wikipedia.org/wiki/Fibonacci_number>`_.

    :param length: The length of the Fibonacci sequence to generate.
    :return: Iterator of the Fibonacci sequence.
    """
    if length < 0:
        raise ValueError(f'length must be a non-negative number, got {length}')

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


def collatz(n: int) -> Iterator[int]:
    """
    Generate a Collatz sequence starting from a given integer.

    The `Collatz conjecture <https://en.wikipedia.org/wiki/Collatz_conjecture>`_ is
    defined as:

    Start with any positive integer n. Then each term is obtained from the previous
    term as follows:

    - If the previous term is even, the next term is one half of the previous term.
    - If the previous term is odd, the next term is 3 times the previous term plus 1.

    The conjecture is that no matter what value of n, the sequence will always reach 1.

    :param n: Positive integer.
    :return: Iterator of the Collatz sequence starting with n.
    """
    if n < 1:
        raise ValueError(f'n must be a positive integer: {n!r}')
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
