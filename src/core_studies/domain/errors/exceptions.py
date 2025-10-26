class DomainError(Exception):
    """Base class for domain-related errors."""
    pass

class AxiomFailedError(DomainError):
    """Raised when a domain axiom fails."""
    pass
