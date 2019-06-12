import unittest

from python_algorithms.data_structures.trees.binary_tree import (
    BinaryTreeNode, traverse
)


class TestBinaryTree(unittest.TestCase):

    def test_traversal(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2, left=BinaryTreeNode(4), right=BinaryTreeNode(5))
        root.right = BinaryTreeNode(3)

        self.assertListEqual(list(traverse(root, order='pre')), [1, 2, 4, 5, 3])
        self.assertListEqual(list(traverse(root, order='in')), [4, 2, 5, 1, 3])
        self.assertListEqual(list(traverse(root, order='post')), [4, 5, 2, 3, 1])
        self.assertListEqual(list(traverse(root, order='level')), [1, 2, 3, 4, 5])
