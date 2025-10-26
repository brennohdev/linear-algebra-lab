from core_studies.domain.ports.Provider import IZeroElementProviderPort
from ...elements.r3_vector import R3Vector

class R3StandardZeroProvider(IZeroElementProviderPort[R3Vector]):
    """
    A provider that implements a IZeroElementProviderPort for R3 vectors
    with the standard zero element (0,0,0).
    """
    
    def get(self) -> R3Vector:
        """
        Get the standard zero element for R3 vectors.
        
        Returns:
            R3Vector: The standard zero element (0,0,0).
        """
        return R3Vector(x=0.0, y=0.0, z=0.0)