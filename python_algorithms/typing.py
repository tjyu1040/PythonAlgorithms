"""Module for custom type-hinting annotations."""
__all__ = ['Comparable']

from typing import TypeVar
import sys

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

T = TypeVar('T')


class ComparableProtocol(Protocol):
    def __ge__(self: T, other: T) -> bool:
        ...

    def __gt__(self: T, other: T) -> bool:
        ...

    def __le__(self: T, other: T) -> bool:
        ...

    def __lt__(self: T, other: T) -> bool:
        ...


Comparable = TypeVar("Comparable", bound=ComparableProtocol)
