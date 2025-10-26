from abc import ABC, abstractmethod


class AlgebraicElement(ABC):
    """
    Represents an abstract element of an algebraic set.

    This is an Abstract Base Class (ABC) that enforces the implementation
    of essential methods so that the axioms of a vector space can be verified.
    """

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Compare whether this element is equal to another.

        Essential to verify axioms like commutativity (u + v == v + u)
        or the existence of the neutral element (v + 0 == v).
        """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """
        Return an "official" string representation of the element.

        Essential for debugging, logs, and to present clear results
        when API axiom checks fail.
        Ex: "Vector(2, 1, 4)" or "Polynomial(2 + x + 4x^2)"
        """
        ...
