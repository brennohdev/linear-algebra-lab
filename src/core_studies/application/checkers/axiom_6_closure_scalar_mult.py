from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckClosureScalarMult(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 6:
    Closure under scalar multiplication (k * u belongs to V).
    """

    @property
    def axiom_name(self) -> str:
        return "A6: Closure under scalar multiplication"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks whether scalar multiplication of a sample element
        still belongs to the set, using the validator.
        """
        try:
            elements = space.element_provider.get_elements(NUM_SAMPLES)
            scalars = space.element_provider.get_scalars(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements or scalars: {e}")

        for i in range(NUM_SAMPLES):
            u = elements[i]
            k = scalars[i]

            try:
                result = space.scalar_multiplication.execute(k, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Multiplication operation failed for {k} * {u}. Error: {e}"
                )

            if not space.validator.validate(result):
                raise AxiomFailedError(
                    f"Result '{result}' of '{k} * {u}' does not belong to the set."
                )
        
        return None
