from typing import TypeVar, Generic, List, Dict, Any
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)


class CheckVectorSpaceUseCase(Generic[ET]):
    """
    Orchestrates the verification of a VectorSpace.

    This use case is an "Orchestrator", not a "Doer".
    It delegates the actual verification work for each axiom
    to the injected checkers.
    """

    def __init__(self, axiom_checkers: List[IAxiomCheckerPort[ET]]): 
        """
        Injects the list of axiom verification strategies.

        Args:
            axiom_checkers: A list of objects implementing
                            the IAxiomCheckerPort interface.
        """
        self._checkers = axiom_checkers

    def execute(self, space: VectorSpace[ET]) -> Dict[str, Any]: 
        """
        Executes the full verification of the vector space.

        Args:
            space: The VectorSpace domain instance to be tested.

        Returns:
            A dictionary (our response DTO) indicating success or listing failures.
        """
        failed_axioms: List[Dict[str, str]] = []

        for checker in self._checkers:
            try:
                checker.check(space)

            except AxiomFailedError as e:
                failed_axioms.append({
                    "axiom": checker.axiom_name,
                    "reason": str(e)
                })
            except Exception as e:
                failed_axioms.append({
                    "axiom": checker.axiom_name,
                    "reason": f"Unexpected error during check: {e}"
                })

        if failed_axioms:
            return {"is_vector_space": False, "failures": failed_axioms}

        return {"is_vector_space": True, "failures": []}
