from typing import TypeVar, Generic, Type

from ..ports.Operations import IAdditionPort, IScalarMultPort
from ..ports.Provider import IZeroElementProviderPort, IAdditiveInverseProviderPort
from .Element import AlgebraicElement

ET = TypeVar('ET', bound=AlgebraicElement)


class VectorSpace(Generic[ET]):
    """
    Represents the domain entity of a Vector Space.

    This class is an "aggregate" that groups:
    1. An element type (e.g., R3Vector)
    2. The implementations (Adapters/Strategies) of the Operation and Provider
       Ports that act on those elements.

    It is agnostic to the concrete implementation, depending only
    on the interfaces (Ports) defined in the domain.
    """

    def __init__(
        self,
        element_type: Type[ET],
        addition_strategy: IAdditionPort,
        scalar_mult_strategy: IScalarMultPort,
        zero_element_provider: IZeroElementProviderPort,
        add_inverse_provider: IAdditiveInverseProviderPort
    ):
        """
        Constructs the Vector Space by injecting its dependencies
        (the implementations of the Ports).
        """
        self._element_type = element_type
        self.addition = addition_strategy
        self.scalar_multiplication = scalar_mult_strategy
        self.zero_element_provider = zero_element_provider
        self.additive_inverse_provider = add_inverse_provider

    @property
    def element_type(self) -> Type[ET]:
        """Returns the element type this space operates on (e.g., R3Vector)."""
        return self._element_type

    def __repr__(self) -> str:
        """Clear representation for debugging."""
        return (f"<VectorSpace operating on {self._element_type.__name__} "
                f"with AddStrategy: {self.addition.__class__.__name__}, "
                f"MultStrategy: {self.scalar_multiplication.__class__.__name__}>")