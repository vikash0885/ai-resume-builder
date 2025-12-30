from fastapi import APIRouter, HTTPException, Body, Request
from pydantic import BaseModel
from typing import List
from ..services.gemini import gemini_service
from ..models.resume import ResumeCreate, ResumeInDB
from ..db.mongodb import db

router = APIRouter()

class PolishRequest(BaseModel):
    text: str

class PolishResponse(BaseModel):
    polished_text: str

@router.post("/", response_model=ResumeInDB)
async def create_resume(resume: ResumeCreate):
    resume_dict = resume.dict()
    new_resume = await db.get_db()["resumes"].insert_one(resume_dict)
    created_resume = await db.get_db()["resumes"].find_one({"_id": new_resume.inserted_id})
    # Helper to convert ObjectId to str
    created_resume["_id"] = str(created_resume["_id"])
    return created_resume

@router.get("/", response_model=List[ResumeInDB])
async def list_resumes():
    resumes = []
    cursor = db.get_db()["resumes"].find()
    async for document in cursor:
        document["_id"] = str(document["_id"])
        resumes.append(document)
    return resumes

@router.post("/polish", response_model=PolishResponse)
async def polish_text(request: PolishRequest):
    # Just polish for now, saving is a separate step usually, but for this demo we return polished text
    polished = await gemini_service.polish_bullet_point(request.text)
    return {"polished_text": polished}

