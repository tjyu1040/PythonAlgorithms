import string
import random
import unittest

import numpy as np

from python_algorithms.math.magic_squares import DuererSquare, MAGIC_SQUARES


def generate_random_string(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


class TestMagicSquares(unittest.TestCase):

    def test_magic_squares(self):
        for magic_square in MAGIC_SQUARES:
            self.assertIsMagicSquare(magic_square)

    def test_magic_square_cryptography(self):
        with self.assertRaises(ValueError):
            test_string = generate_random_string(size=4)
            DuererSquare.encode(test_string)

        for value in (0, 0.0, set(), dict()):
            with self.assertRaises(TypeError):
                DuererSquare.encode(value)
            with self.assertRaises(TypeError):
                DuererSquare.decode(value)

        test_string = 'THISISAMATHTEST.'
        expected_encoded_string = '.IHEITHMASATSTST'
        encoded_string = DuererSquare.encode(test_string)
        self.assertEqual(encoded_string, expected_encoded_string)
        decoded_string = DuererSquare.decode(encoded_string)
        self.assertEqual(decoded_string, test_string)

        test_square = np.array(list(test_string)).reshape(4, 4)
        encoded_square = DuererSquare.encode(test_string, expand=True)
        decoded_square = DuererSquare.decode(encoded_square)
        np.testing.assert_array_equal(test_square, decoded_square)

    def assertIsMagicSquare(self, magic_square):
        name = magic_square.name
        constant = magic_square.constant
        square = magic_square.square

        n, m = square.shape
        self.assertEqual(n, m, msg='{} is not a square: {!r}'.format(name, square.shape))

        sorted_flattened_array = np.sort(np.ravel(square))
        expected_flattened_array = np.arange(1, n ** 2 + 1)
        np.testing.assert_equal(
            sorted_flattened_array, expected_flattened_array,
            err_msg='{} does not contain distinct positive integers from 1 to {}.'.format(
                name, n ** 2 + 1
            )
        )

        self.assertLineSum(square, constant, axis=0)
        self.assertLineSum(square, constant, axis=1)

    def assertLineSum(self, square, constant, axis):
        line_sums = np.sum(square, axis=axis)
        self.assertTrue(np.all(line_sums == constant))
