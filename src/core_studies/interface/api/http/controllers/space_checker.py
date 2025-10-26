from fastapi import APIRouter, HTTPException, status
from typing import Any

from .....containers import DependencyContainer

router = APIRouter()

container = DependencyContainer()

@router.post("/check-space/{space_name}", response_model=dict[str, Any])
async def check_vector_space_endpoint(space_name: str):
    """
    Endpoint to verify whether a predefined vector space
    satisfies the 10 axioms.

    Args:
        space_name (str): The name of the space "recipe" to be tested
                          (e.g. "R3_STANDARD", "R3_RULE_X_ONLY_MULT").

    Returns:
        A dictionary with the key "is_vector_space" (bool) and,
        on failure, a "failures" list detailing the axioms
        that were not satisfied.

    Raises:
        HTTPException(404): If 'space_name' is unknown.
        HTTPException(500): For unexpected errors during execution.
    """
    try:
        use_case = container.provide_vector_space_use_case()
        space_to_test = container.provide_space(space_name)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error assembling dependencies: {e}"
        )

    try:
        result = use_case.execute(space_to_test)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during execution of the check: {e}"
        )
