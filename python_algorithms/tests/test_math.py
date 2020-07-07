import unittest

from python_algorithms.math import lcm, gcd


class TestMath(unittest.TestCase):

    def test_gcd(self):
        for a, b in [(0.5, 1), (1, 0.5)]:
            with self.assertRaises(TypeError):
                gcd(a, b)

    def test_lcm(self):
        for a, b in [(0.5, 1), (1, 0.5)]:
            with self.assertRaises(TypeError):
                lcm(a, b)

        with self.assertRaises(RuntimeError):
            lcm(0, 0)
