from typing import List, Dict, Any

from .domain.entities.VectorSpace import VectorSpace

from .application.use_cases.check_vector_space import CheckVectorSpaceUseCase
from .application.ports.axiom_checker import IAxiomCheckerPort as ICheckerPort
from .application.checkers.axiom_1_closure_addition import CheckClosureAddition
from .application.checkers.axiom_2_commutativity import CheckCommutativity
from .application.checkers.axiom_3_associativity import CheckAssociativity
from .application.checkers.axiom_4_neutral_element import CheckNeutralElement
from .application.checkers.axiom_5_additive_inverse import CheckAdditiveInverse
from .application.checkers.axiom_6_closure_scalar_mult import CheckClosureScalarMult
from .application.checkers.axiom_7_distributivity_vec import CheckDistributivityVec
from .application.checkers.axiom_8_distributivy_scalar import CheckDistributivityScalar 
from .application.checkers.axiom_9_associativity_scalar import CheckAssociativityScalar
from .application.checkers.axiom_10_identity_mult import CheckIdentityMult

from .infrastructure.elements.r3_vector import R3Vector
from .infrastructure.adapters.addition.standard_r3_addition import StandardR3AdditionAdapter as StandardR3Addition
from .infrastructure.adapters.multiplication.r3_standard_scalar_mult import R3StandardScalarMult as R3StandardScalarMult
from .infrastructure.adapters.multiplication.r3_x_only_scalar_mult import R3XOnlyScalarMultAdapter
from .infrastructure.adapters.providers.r3_standard_zero_provider import R3StandardZeroProvider
from .infrastructure.adapters.providers.r3_standard_inverse_provider import R3StandardInverseProvider
from .infrastructure.adapters.providers.r3_standard_element_provider import R3StandardElementProvider
from .infrastructure.adapters.validators.r3_standard_validator import R3StandardValidator


class DependencyContainer:
    """
    This container (factory) assembles services and dependencies.
    """
    
    def __init__(self):
        self._adapters: Dict[str, Any] = {
            "R3Vector": R3Vector,
            "StandardR3Addition": StandardR3Addition(),
            "R3StandardScalarMult": R3StandardScalarMult(),
            "R3XOnlyScalarMultAdapter": R3XOnlyScalarMultAdapter(),
            "R3StandardZeroProvider": R3StandardZeroProvider(),
            "R3StandardInverseProvider": R3StandardInverseProvider(),
            "R3StandardElementProvider": R3StandardElementProvider(),
            "R3StandardValidator": R3StandardValidator(),
        }

        self._checkers: List[ICheckerPort[Any]] = [
            CheckClosureAddition(),
            CheckCommutativity(),
            CheckAssociativity(),
            CheckNeutralElement(),
            CheckAdditiveInverse(),
            CheckClosureScalarMult(),
            CheckDistributivityVec(),
            CheckDistributivityScalar(),
            CheckAssociativityScalar(),
            CheckIdentityMult(),
        ]

    def provide_vector_space_use_case(self) -> CheckVectorSpaceUseCase[Any]:
        """
        RECIPE 1: Builds the "Engine" (the main Use Case).
        """
        return CheckVectorSpaceUseCase(
            axiom_checkers=self._checkers 
        )

    def provide_space(self, space_name: str) -> VectorSpace[Any]:
        """
        RECIPE 2: Builds a "Vector Space" (the test object)
        based on a predefined "recipe".
        """
        
        if space_name == "R3_STANDARD":
            return VectorSpace[R3Vector](
                element_type=self._adapters["R3Vector"],
                addition_strategy=self._adapters["StandardR3Addition"],
                scalar_mult_strategy=self._adapters["R3StandardScalarMult"],
                zero_element_provider=self._adapters["R3StandardZeroProvider"],
                add_inverse_provider=self._adapters["R3StandardInverseProvider"],
                element_provider=self._adapters["R3StandardElementProvider"],
                validator=self._adapters["R3StandardValidator"]
            )
        
        if space_name == "R3_RULE_X_ONLY_MULT":
            return VectorSpace[R3Vector](
                element_type=self._adapters["R3Vector"],
                addition_strategy=self._adapters["StandardR3Addition"],
                scalar_mult_strategy=self._adapters["R3XOnlyScalarMultAdapter"],
                zero_element_provider=self._adapters["R3StandardZeroProvider"],
                add_inverse_provider=self._adapters["R3StandardInverseProvider"],
                element_provider=self._adapters["R3StandardElementProvider"],
                validator=self._adapters["R3StandardValidator"]
            )
        
        raise ValueError(f"Unknown space recipe: '{space_name}'")
