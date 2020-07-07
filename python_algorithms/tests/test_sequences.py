from types import GeneratorType
from typing import List
import unittest

from numpy.testing import assert_array_equal

from python_algorithms.sequences import fibonacci_number, fibonacci_sequence


class TestSequences(unittest.TestCase):

    def test_fibonacci_number(self):
        # Further tests are already covered through doctests in the function's docstring.
        with self.assertRaises(ValueError):
            fibonacci_number(-1)

    def test_fibonacci_sequence(self):
        with self.assertRaises(ValueError):
            next(fibonacci_sequence(-1))

        sequence = fibonacci_sequence(0)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = []  # type: List[int]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(1)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(5)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3]
        assert_array_equal(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(10)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert_array_equal(expected_sequence, list(sequence))
