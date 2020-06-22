from types import GeneratorType
import unittest

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
        expected_sequence = []
        self.assertListEqual(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(1)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0]
        self.assertListEqual(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(5)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3]
        self.assertListEqual(expected_sequence, list(sequence))

        sequence = fibonacci_sequence(10)
        self.assertIsInstance(sequence, GeneratorType)
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertListEqual(expected_sequence, list(sequence))
