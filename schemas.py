from pydantic import BaseModel, ConfigDict

class ResumeBase(BaseModel):
    name: str
    email: str
    skills: str
    experience: str

class ResumeCreate(ResumeBase):
    pass

class ResumeOut(ResumeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
