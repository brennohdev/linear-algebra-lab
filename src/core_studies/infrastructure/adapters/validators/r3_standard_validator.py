from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.ports.Validator import IElementValidatorPort
from ...elements.r3_vector import R3Vector


class R3StandardValidator(IElementValidatorPort[R3Vector]):
    """
    This adapter implements IElementValidatorPort with the logic
    specific to the standard R^3 set.

    For standard R^3, any R3Vector is considered valid.
    """

    def validate(self, element: AlgebraicElement) -> bool:
        """
        Checks whether the element belongs to the R^3 set.

        Args:
            element: The element to be validated.

        Returns:
            True if it is an R3Vector, False otherwise.
        """
        if isinstance(element, R3Vector):
            return True

        return False