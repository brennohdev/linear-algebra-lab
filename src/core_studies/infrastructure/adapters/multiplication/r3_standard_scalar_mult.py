from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.ports.Operations import IScalarMultPort, Scalar
from ...elements.r3_vector import R3Vector


class R3StandardScalarMult(IScalarMultPort):
    def execute(self, scalar: Scalar, element: AlgebraicElement) -> AlgebraicElement:
        if not isinstance(element, R3Vector):
            raise TypeError("R3StandardScalarMult can only operate on R3Vector instances.")

        result_x = scalar * element.x
        result_y = scalar * element.y
        result_z = scalar * element.z

        return R3Vector(x=result_x, y=result_y, z=result_z)
