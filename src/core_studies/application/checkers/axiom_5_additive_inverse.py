from typing import TypeVar, Generic 
from core_studies.application.ports.axiom_checker import IAxiomCheckerPort
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckAdditiveInverse(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implements the check for Axiom 5:
    Existence of an Additive Inverse (u + (-u) = 0).
    """

    @property
    def axiom_name(self) -> str:
        return "A5: Existence of Additive Inverse"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Checks that, for each sample element 'u',
        its inverse '-u' provided by the provider
        satisfies u + (-u) = 0.
        """
        
        try:
            zero = space.zero_element_provider.get()
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain zero element (dependency Axiom 4): {e}")

        try:
            samples = space.element_provider.get_elements(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Failed to obtain sample elements: {e}")

        for u in samples:
            try:
                inv_u = space.additive_inverse_provider.get_inverse_of(u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Failed to obtain inverse of '{u}'. Error: {e}"
                )

            if not space.validator.validate(inv_u):
                raise AxiomFailedError(
                    f"The provided inverse '{inv_u}' for element '{u}' "
                    f"does not belong to the set (validator failed)."
                )

            try:
                u_plus_inv_u = space.addition.execute(u, inv_u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed when computing {u} + {inv_u}. Error: {e}"
                )
            
            if u_plus_inv_u != zero:
                raise AxiomFailedError(
                    f"Rule u + (-u) = 0 failed. "
                    f"'{u} + {inv_u}' resulted in '{u_plus_inv_u}', but should be the zero '{zero}'."
                )

            try:
                inv_u_plus_u = space.addition.execute(inv_u, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"Operation failed when computing {inv_u} + {u}. Error: {e}"
                )
            
            if inv_u_plus_u != zero:
                raise AxiomFailedError(
                    f"Rule (-u) + u = 0 failed. "
                    f"'{inv_u} + {u}' resulted in '{inv_u_plus_u}', but should be the zero '{zero}'."
                )
        
        return None