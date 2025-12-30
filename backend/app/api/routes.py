from fastapi import APIRouter
from . import resumes

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

router.include_router(resumes.router, prefix="/resumes", tags=["resumes"])
