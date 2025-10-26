from abc import ABC, abstractmethod

from ..entities.Element import AlgebraicElement


class IZeroElementProviderPort(ABC):
    """
    Port (Interface) for a Strategy that provides
    the neutral (zero) element of the set.
    """

    @abstractmethod
    def get(self) -> AlgebraicElement:
        """Returns the additive identity element."""
        ...


class IAdditiveInverseProviderPort(ABC):
    """
    Port (Interface) for a Strategy that provides
    the additive inverse of a given element.
    """

    @abstractmethod
    def get_inverse_of(self, element: AlgebraicElement) -> AlgebraicElement:
        """
        Receives an element and returns its additive inverse.
        E.g., for v returns -v
        """
        ...