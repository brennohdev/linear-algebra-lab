from dataclasses import dataclass, field 
import math 

from core_studies.domain.entities.Element import AlgebraicElement

@dataclass(frozen=True)
class R3Vector(AlgebraicElement):
    """
    Represents a vector in 3-dimensional Euclidean space (R³).
    ... uses math.isclose for floating point comparisons.
    """
    x: float
    y: float
    z: float
    _tolerance: float = field(default=1e-9, compare=False, repr=False, hash=False)

    def __eq__(self, other: object) -> bool:
        """
        Compares this vector to another, using tolerance for floats.
        """
        if not isinstance(other, R3Vector):
            return NotImplemented # Important for compatibility
        
        return (
            math.isclose(self.x, other.x, abs_tol=self._tolerance) and
            math.isclose(self.y, other.y, abs_tol=self._tolerance) and
            math.isclose(self.z, other.z, abs_tol=self._tolerance)
        )

    def __repr__(self) -> str:
        """Return representation of the vector."""
        return f"R3Vector(x={self.x}, y={self.y}, z={self.z})"