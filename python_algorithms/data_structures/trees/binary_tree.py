""" Module containing abstract binary tree structure and algorithms. """
from abc import ABC, abstractmethod

import attr


@attr.s
class BinaryTreeNode(object):

    element = attr.ib()

    left = attr.ib(None)

    right = attr.ib(None)

    def __len__(self):
        return compute_size(self)

    @property
    def height(self):
        return compute_height(self)

    def traverse(self, order='pre'):
        return traverse(self, order)


@attr.s
class BinaryTree(ABC):
    """ Abstract binary tree class. """

    _root = attr.ib(None)

    def __len__(self):
        return compute_size(self._root)

    @property
    def height(self):
        return compute_height(self._root)

    def traverse(self, order='pre'):
        return traverse(self._root, order)

    @abstractmethod
    def insert(self, element):
        pass

    @abstractmethod
    def remove(self, element):
        pass

    @abstractmethod
    def __contains__(self, element):
        pass


def compute_size(root):
    if root is None:
        return 0
    left_size = compute_size(root.left)
    right_size = compute_size(root.right)
    return left_size + right_size + 1


def compute_height(root):
    if root is None:
        return 0
    left_height = compute_height(root.left)
    right_height = compute_height(root.right)
    return max(left_height, right_height) + 1


def traverse(root, order='pre'):
    if order not in ['pre', 'in', 'post', 'level']:
        msg = '{} order traversal is not supported.'
        raise ValueError(msg.format(order))

    if root:
        if order == 'pre':
            yield root.element
            yield from traverse(root.left, order)
            yield from traverse(root.right, order)
        elif order == 'in':
            yield from traverse(root.left, order)
            yield root.element
            yield from traverse(root.right, order)
        elif order == 'post':
            yield from traverse(root.left, order)
            yield from traverse(root.right, order)
            yield root.element
        elif order == 'level':
            queue = [root]
            while len(queue) > 0:
                node = queue.pop(0)
                yield node.element
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
