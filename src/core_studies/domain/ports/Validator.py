from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ..entities.Element import AlgebraicElement

ET = TypeVar('ET', bound=AlgebraicElement)


class IElementValidatorPort(Generic[ET], ABC):
    """
    Port (Interface) for a Strategy that validates
    whether an element belongs to the set.
    (e.g., for Exercise I.6, whether the matrix has 1's on the diagonal)
    """
    @abstractmethod
    def validate(self, element: AlgebraicElement) -> bool:
        """
        Returns True if the element belongs to the set,
        False otherwise.
        """
        ...