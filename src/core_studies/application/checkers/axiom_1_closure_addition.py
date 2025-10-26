from typing import TypeVar, Generic
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckClosureAddition(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 1:
    Closure under addition (u + v belongs to V).
    """

    @property
    def axiom_name(self) -> str:
        return "A1: Closure under Addition"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks whether the sum of two sample elements
        still belongs to the set, using the space's validator.
        """
        try:
            samples = space.element_provider.get_elements(NUM_SAMPLES * 2)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements: {e}")

        for i in range(NUM_SAMPLES):
            u = samples[i]
            v = samples[i + NUM_SAMPLES]

            try:
                result = space.addition.execute(u, v)
            except Exception as e:
                raise AxiomFailedError(
                    f"Addition operation failed for {u} + {v}. Error: {e}"
                )

            if not space.validator.validate(result):
                raise AxiomFailedError(
                    f"Result '{result}' of '{u} + {v}' does not belong to the set."
                )
        
        return None
