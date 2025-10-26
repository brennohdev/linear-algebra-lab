from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.ports.Operations import IAdditionPort
from ...elements.r3_vector import R3Vector

class StandardR3AdditionAdapter(IAdditionPort):
    """
    An adapter that implements addition for R3 vectors
    with the logical standard addition operation.
    (x,y,z) + (a,b,c) = (x+a, y+b, z+c)
    """
    
    def execute(self, e1: AlgebraicElement, e2: AlgebraicElement) -> AlgebraicElement:
        """
        Execute the addition operation for two R3 vectors.
        
        Args:
            e1 (AlgebraicElement): The first R3 vector.
            e2 (AlgebraicElement): The second R3 vector.
        
        Returns:
            AlgebraicElement: The resulting R3 vector after addition.
        
        Raises:
            TypeError: If either e1 or e2 is not an instance of R3Vector.
        """
        if not isinstance(e1, R3Vector) or not isinstance(e2, R3Vector):
            raise TypeError("Both elements must be instances of R3Vector.")

        result_x = e1.x + e2.x
        result_y = e1.y + e2.y
        result_z = e1.z + e2.z
        
        return R3Vector(x=result_x, y=result_y, z=result_z)