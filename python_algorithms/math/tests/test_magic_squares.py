import unittest

import numpy as np

from python_algorithms.math.magic_squares import MAGIC_SQUARES


class TestMagicSquares(unittest.TestCase):

    def test_magic_squares(self):
        for magic_square in MAGIC_SQUARES:
            self.assertIsMagicSquare(magic_square)

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
