import random
import unittest

from python_algorithms.searches import binary_search


def generate_random_items(length=1000000, num_samples=1000):
    return random.sample(range(-length, length), num_samples)


class TestSearches(unittest.TestCase):

    def test_binary_search(self):
        index = binary_search([], 10)
        self.assertEqual(index, -1)

        with self.assertRaisesRegex(ValueError, r'array must be sorted'):
            binary_search([1, -1], 1)

        items = sorted(range(5))
        index = binary_search(items, -100)
        self.assertEqual(index, -1)
        index = binary_search(items, 100)
        self.assertEqual(index, -1)

        items = sorted(generate_random_items())
        for expected_index, item in enumerate(items):
            index = binary_search(items, item)
            self.assertEqual(index, expected_index)
