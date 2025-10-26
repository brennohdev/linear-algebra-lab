from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3


class CheckCommutativity(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 2:
    Commutativity of Addition (u + v = v + u).
    """

    @property
    def axiom_name(self) -> str:
        return "A2: Commutativity of Addition"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Verifies that u + v == v + u for several sample pairs.
        """
        try:
            samples = space.element_provider.get_elements(NUM_SAMPLES * 2)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements: {e}")

        for i in range(NUM_SAMPLES):
            u = samples[i]
            v = samples[i + NUM_SAMPLES]

            try:
                les = space.addition.execute(u, v)
            except Exception as e:
                raise AxiomFailedError(
                    f"The addition operation failed for {u} + {v}. Error: {e}"
                )

            try:
                lde = space.addition.execute(v, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"The addition operation failed for {v} + {u}. Error: {e}"
                )

            if les != lde:
                raise AxiomFailedError(
                    f"Failure: {u} + {v} resulted in '{les}', "
                    f"but {v} + {u} resulted in '{lde}'."
                )
        
        return None