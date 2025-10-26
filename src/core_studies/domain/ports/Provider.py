from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from ..entities.Element import AlgebraicElement
from .Operations import Scalar

ET = TypeVar('ET', bound=AlgebraicElement)


class IZeroElementProviderPort(Generic[ET], ABC):
    """
    Interface for a strategy that provides the neutral (zero) element of the set.
    """
    @abstractmethod
    def get(self) -> ET:
        ...


class IAdditiveInverseProviderPort(Generic[ET], ABC):
    """
    Interface for a strategy that provides the additive inverse of a given element.
    """
    @abstractmethod
    def get_inverse_of(self, element: ET) -> ET:
        ...


class IElementProviderPort(Generic[ET], ABC):
    """
    Interface for a strategy that provides sample elements and scalars for axiom tests.
    """
    @abstractmethod
    def get_elements(self, count: int) -> List[ET]:
        """Return a list of 'count' sample elements."""
        ...

    @abstractmethod
    def get_scalars(self, count: int) -> List[Scalar]:
        """Return a list of 'count' sample scalars."""
        ...
