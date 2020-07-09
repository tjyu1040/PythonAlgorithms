"""Module containing search algorithms."""
__all__ = ['binary_search']

from typing import Sequence

from python_algorithms.typing import Comparable


def binary_search(array: Sequence[Comparable], item: Comparable) -> int:
    """
    Search for an item in a sorted array using binary search algorithms.

    Binary search compares the target value to the middle element of the array. If they
    are not equal, the half in which the target cannot lie is eliminated and the search
    continues on the remaining half, again taking the middle element to compare to the
    target value, and repeating this until the target value is found. If the search ends
    with the remaining half being empty, the target is not in the array.

    :param array: Sorted array of comparable items.
    :param item: A comparable item to search for.
    :return: The index of the item in the array. If not found, -1 will be returned.
    """
    if not is_sorted(array):
        raise ValueError(f'array must be sorted: {array!r}')

    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < item:
            left_index = mid_index + 1
        elif array[mid_index] > item:
            right_index = mid_index - 1
        else:
            return mid_index
    return -1


def is_sorted(array: Sequence[Comparable]) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
