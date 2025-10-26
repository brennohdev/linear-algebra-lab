from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.ports.Provider import IAdditiveInverseProviderPort

from ...elements.r3_vector import R3Vector

class R3StandardInverseProvider(IAdditiveInverseProviderPort[R3Vector]):
    """
    A provider that implements an IAdditiveInverseProviderPort for a R3 vector
    with the specific logic to find the additive inverse.
    For a vector (x,y,z), its additive inverse is (-x,-y,-z).
    """
    
    def get_inverse_of(self, element: AlgebraicElement) -> R3Vector:
        """
        Returns the additive inverse of a given R3Vector element.

        Args:
            element: The element 'u' (must be an R3Vector).

        Returns:
            A new R3Vector representing '-u'.
        
        Raises:
            TypeError: If the element is not an R3Vector.
        """
        if not isinstance(element, R3Vector):
            raise TypeError(
                "R3StandardInverseProvider can only operate on R3Vector instances."
            )

        result_x = -element.x
        result_y = -element.y
        result_z = -element.z

        return R3Vector(x=result_x, y=result_y, z=result_z)