from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckAssociativity(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 3:
    Additive associativity ((u + v) + w = u + (v + w)).
    """

    @property
    def axiom_name(self) -> str:
        return "A3: Additive Associativity"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks whether (u + v) + w == u + (v + w) for several triples.
        """
        try:
            samples = space.element_provider.get_elements(NUM_SAMPLES * 3)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements: {e}")

        for i in range(NUM_SAMPLES):
            u = samples[i]
            v = samples[i + NUM_SAMPLES]
            w = samples[i + (NUM_SAMPLES * 2)]

            try:
                temp_uv = space.addition.execute(u, v)
                left = space.addition.execute(temp_uv, w)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed when computing (Left Side) "
                    f"({u} + {v}) + {w}. Error: {e}"
                )

            try:
                temp_vw = space.addition.execute(v, w)
                right = space.addition.execute(u, temp_vw)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed when computing (Right Side) "
                    f"{u} + ({v} + {w}). Error: {e}"
                )

            if left != right:
                raise AxiomFailedError(
                    f"Failure: ({u} + {v}) + {w} resulted in '{left}', "
                    f"but {u} + ({v} + {w}) resulted in '{right}'."
                )
        
        return None