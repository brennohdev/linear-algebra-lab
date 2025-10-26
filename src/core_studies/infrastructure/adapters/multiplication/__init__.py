from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.ports.Operations import IScalarMultPort, Scalar
from ...elements.r3_vector import R3Vector


class R3StandardScalarMult(IScalarMultPort):
    """
    This adapter implements IScalarMultPort with the logic
    specific to standard scalar multiplication in R^3.
    k * (x,y,z) = (kx, ky, kz)
    """

    def execute(self, scalar: Scalar, element: AlgebraicElement) -> AlgebraicElement:
        """
        Executes the standard multiplication in R^3.

        Args:
            scalar: The scalar 'k'.
            element: The element (must be an R3Vector).

        Returns:
            A *new* R3Vector with the result of the operation.

        Raises:
            TypeError: If the element is not an R3Vector.
        """
        if not isinstance(element, R3Vector):
            raise TypeError(
                "R3StandardScalarMult can only operate on R3Vectors."
            )

        result_x = scalar * element.x
        result_y = scalar * element.y
        result_z = scalar * element.z

        return R3Vector(x=result_x, y=result_y, z=result_z)