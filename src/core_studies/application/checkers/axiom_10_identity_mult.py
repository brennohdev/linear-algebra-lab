"""
Application Module: Checker for Axiom 10 (Multiplicative Identity)
"""

from typing import TypeVar, Generic
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort as ICheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3

class CheckIdentityMult(Generic[ET], ICheckerPort[ET]):
    """
    Implements verification for Axiom 10:
    Multiplicative Identity (1 * u = u).
    """

    @property
    def axiom_name(self) -> str:
        return "A10: Multiplicative Identity"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks that 1 * u == u for several sample elements.
        """
        try:
            elements = space.element_provider.get_elements(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements: {e}")

        for u in elements:
            scalar = 1

            try:
                les = space.scalar_multiplication.execute(scalar, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed while calculating {scalar} * {u}. Error: {e}"
                )

            if les != u:
                raise AxiomFailedError(
                    f"Failure: {scalar} * {u} resulted in '{les}', but it should be the element itself '{u}'."
                )

        return None
