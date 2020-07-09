import unittest

import numpy as np

from python_algorithms.math.numbers import lcm, gcd


class TestNumbers(unittest.TestCase):

    def setUp(self):
        self.invalid_integers = [(0.5, 1), (1, 0.5), (0.5, 0, 0.5), ('a', 'b')]

    def test_gcd(self):
        with self.assertRaisesRegex(ValueError, r'integers must not be empty'):
            gcd()

        for values in self.invalid_integers:
            with self.assertRaises(TypeError):
                gcd(*values)  # type: ignore

        # Test that this works with numpy integers as well.
        result = gcd(*np.array([2, 8, 10], dtype=int))
        self.assertEqual(2, result)

    def test_lcm(self):
        with self.assertRaisesRegex(ValueError, r'integers must not be empty'):
            lcm()

        for values in self.invalid_integers:
            with self.assertRaises(TypeError):
                lcm(*values)  # type: ignore

        with self.assertRaisesRegex(RuntimeError, r'lcm\(0, 0\) is undefined'):
            lcm(0, 0)

        # Test that this works with numpy integers as well.
        result = lcm(*np.array([2, 8, 10], dtype=int))
        self.assertEqual(40, result)
