from abc import ABC, abstractmethod

Scalar = int | float

from ..entities.Element import AlgebraicElement


class IAdditionPort(ABC):
    """
    Port (Interface) for an Addition Strategy.

    Defines the contract that any Addition "Adapter" must
    implement to be plugged into a VectorSpace.
    """

    @abstractmethod
    def execute(self, e1: AlgebraicElement, e2: AlgebraicElement) -> AlgebraicElement:
        """Receives two elements and returns their sum."""
        ...


class IScalarMultPort(ABC):
    """
    Port (Interface) for a Scalar Multiplication Strategy.

    Defines the contract that any Multiplication "Adapter"
    must implement.
    """

    @abstractmethod
    def execute(self, scalar: Scalar, element: AlgebraicElement) -> AlgebraicElement:
        """
        Receives a scalar and an element, and returns the
        result of the scalar multiplication.
        """
        ...