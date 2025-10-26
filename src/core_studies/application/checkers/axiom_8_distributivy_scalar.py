from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3

class CheckDistributivityScalar(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 8:
    Distributivity (k + l) * u = k*u + l*u.
    """

    @property
    def axiom_name(self) -> str:
        return "A8: Distributivity (Scalar Addition)"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Verifies that (k + l)*u == k*u + l*u for several triples.
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
                k_plus_l = k + l 
                les = space.scalar_multiplication.execute(k_plus_l, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed while computing (Left Side) "
                    f"({k} + {l}) * {u}. Error: {e}"
                )

            try:
                temp_ku = space.scalar_multiplication.execute(k, u)
                temp_lu = space.scalar_multiplication.execute(l, u)
                lde = space.addition.execute(temp_ku, temp_lu)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed while computing (Right Side) "
                    f"({k} * {u}) + ({l} * {u}). Error: {e}"
                )

            if les != lde:
                raise AxiomFailedError(
                    f"Failure: ({k} + {l}) * {u} resulted in '{les}', "
                    f"but ({k} * {u}) + ({l} * {u}) resulted in '{lde}'."
                )
        
        return None