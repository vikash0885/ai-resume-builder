from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

class ResumeBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    experience_raw: str
    polished_experience: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResumeCreate(ResumeBase):
    pass

class ResumeInDB(ResumeBase):
    id: str = Field(..., alias="_id")
