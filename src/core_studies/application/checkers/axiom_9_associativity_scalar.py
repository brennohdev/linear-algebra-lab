from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3


class CheckAssociativityScalar(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 9:
    Associativity (k * l) * u = k * (l * u).
    """

    @property
    def axiom_name(self) -> str:
        return "A9: Associativity of Scalar Multiplication"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Verifies that (k * l) * u == k * (l * u) for several triples.
        """
        try:
            scalars_k = space.element_provider.get_scalars(NUM_SAMPLES)
            scalars_l = space.element_provider.get_scalars(NUM_SAMPLES)
            elements = space.element_provider.get_elements(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements or scalars: {e}")

        for i in range(NUM_SAMPLES):
            k = scalars_k[i]
            l = scalars_l[i]
            u = elements[i]

            try:
                k_times_l = k * l
                left_result = space.scalar_multiplication.execute(k_times_l, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"The operation failed while computing (Left Side) "
                    f"({k} * {l}) * {u}. Error: {e}"
                )

            try:
                temp_lu = space.scalar_multiplication.execute(l, u)
                right_result = space.scalar_multiplication.execute(k, temp_lu)
            except Exception as e:
                raise AxiomFailedError(
                    f"The operation failed while computing (Right Side) "
                    f"{k} * ({l} * {u}). Error: {e}"
                )

            if left_result != right_result:
                raise AxiomFailedError(
                    f"Failure: ({k} * {l}) * {u} resulted in '{left_result}', "
                    f"but {k} * ({l} * {u}) resulted in '{right_result}'."
                )
        
        return None