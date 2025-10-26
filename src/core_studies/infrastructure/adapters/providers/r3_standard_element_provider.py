import random
from typing import List, Tuple
from core_studies.domain.ports.Provider import IElementProviderPort
from core_studies.domain.ports.Operations import Scalar
from ...elements.r3_vector import R3Vector


class R3StandardElementProvider(IElementProviderPort[R3Vector]):
    """
    This adapter implements IElementProviderPort to provide
    random R3Vector vectors and random scalars.
    """

    def __init__(
        self, 
        element_range: Tuple[float, float] = (-10.0, 10.0), 
        scalar_range: Tuple[float, float] = (-5.0, 5.0)
    ):
        """
        Initializes the provider with ranges for generation.
        """
        self._element_min, self._element_max = element_range
        self._scalar_min, self._scalar_max = scalar_range

    def get_elements(self, count: int) -> List[R3Vector]:
        """
        Returns a list of 'count' random R3Vector instances.
        """
        elements: List[R3Vector] = []
        for _ in range(count):
            elements.append(
                R3Vector(
                    x=random.uniform(self._element_min, self._element_max),
                    y=random.uniform(self._element_min, self._element_max),
                    z=random.uniform(self._element_min, self._element_max)
                )
            )
        return elements

    def get_scalars(self, count: int) -> List[Scalar]:
        """
        Returns a list of 'count' random scalars.
        """
        scalars: List[Scalar] = []
        for _ in range(count):
            if random.choice([True, False]):
                scalar = random.uniform(self._scalar_min, self._scalar_max)
            else:
                scalar = float(random.randint(int(self._scalar_min), int(self._scalar_max)))
            scalars.append(scalar)
        
        if count > 0 and 0.0 not in scalars:
            scalars[0] = 0.0
        if count > 1 and 1.0 not in scalars:
            scalars[1] = 1.0
            
        return scalars