from fastapi import FastAPI

from .http.controllers import space_checker

app = FastAPI(
    title="Linear Algebra Analyzer API",
    description="API to verify axioms of vector spaces.",
    version="0.1.0",
)

app.include_router(
    space_checker.router,
    prefix="/v1",
    tags=["Vector Space Checker"], 
)

@app.get("/", tags=["Root"])
async def read_root():
    """Root endpoint to check if the API is online."""
    return {"message": "Linear Algebra Analyzer API is online!"}
