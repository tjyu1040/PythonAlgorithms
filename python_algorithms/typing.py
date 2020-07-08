"""Module for custom type-hinting annotations."""
__all__ = ['Comparable']

from abc import abstractmethod
from typing import Any, TypeVar
import sys
if sys.version_info < (3, 8,):
    from typing_extensions import Protocol
else:
    from typing import Protocol

Comparable = TypeVar("Comparable", bound="ComparableProtocol")


class ComparableProtocol(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: Comparable, other: Comparable) -> bool:
        pass

    def __gt__(self: Comparable, other: Comparable) -> bool:
        return (not self < other) and self != other

    def __le__(self: Comparable, other: Comparable) -> bool:
        return self < other or self == other

    def __ge__(self: Comparable, other: Comparable) -> bool:
        return not self < other
