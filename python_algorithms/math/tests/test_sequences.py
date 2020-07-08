from types import GeneratorType
from typing import List
import unittest

from numpy.testing import assert_array_equal

from python_algorithms.math.sequences import (
    fibonacci_number, fibonacci, collatz
)


class TestSequences(unittest.TestCase):

    def test_fibonacci_number(self):
        # Further tests are already covered through doctests in the function's docstring.
        with self.assertRaises(ValueError):
            fibonacci_number(-1)

    def test_fibonacci_sequence(self):
        with self.assertRaises(ValueError):
            next(fibonacci(-1))

        sequence = fibonacci(0)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = []  # type: List[int]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci(1)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci(5)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci(10)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert_array_equal(expected_sequence, list(sequence))

    def test_collatz(self):
        with self.assertRaises(ValueError):
            next(collatz(0))

        sequence = collatz(12)
        expected_sequence = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
        assert_array_equal(expected_sequence, list(sequence))
