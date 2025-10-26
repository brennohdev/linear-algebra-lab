from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckDistributivityVec(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 7:
    Distributivity k * (u + v) = k*u + k*v.
    """

    @property
    def axiom_name(self) -> str:
        return "A7: Distributivity (Vector Addition)"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks whether k*(u + v) == k*u + k*v for several samples.
        """
        try:
            scalars = space.element_provider.get_scalars(NUM_SAMPLES)
            elements_u = space.element_provider.get_elements(NUM_SAMPLES)
            elements_v = space.element_provider.get_elements(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements or scalars: {e}")

        for i in range(NUM_SAMPLES):
            k = scalars[i]
            u = elements_u[i]
            v = elements_v[i]

            try:
                temp_uv = space.addition.execute(u, v)
                les = space.scalar_multiplication.execute(k, temp_uv)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed while computing (Left Side) "
                    f"{k} * ({u} + {v}). Error: {e}"
                )

            try:
                temp_ku = space.scalar_multiplication.execute(k, u)
                temp_kv = space.scalar_multiplication.execute(k, v)
                lde = space.addition.execute(temp_ku, temp_kv)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed while computing (Right Side) "
                    f"({k} * {u}) + ({k} * {v}). Error: {e}"
                )

            if les != lde:
                raise AxiomFailedError(
                    f"Failure: {k} * ({u} + {v}) resulted in '{les}', "
                    f"but ({k} * {u}) + ({k} * {v}) resulted in '{lde}'."
                )
        
        return None