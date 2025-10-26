from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace

ET = TypeVar('ET', bound=AlgebraicElement)

class IAxiomCheckerPort(Generic[ET], ABC):
    @property
    @abstractmethod
    def axiom_name(self) -> str:
        """Returns the name of the axiom being checked."""
        pass
    
    @abstractmethod
    def check(self, space: VectorSpace[ET]) -> None:
        pass