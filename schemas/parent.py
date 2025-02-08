from pydantic import BaseModel

class ParentBase(BaseModel):
    name: str
    mobile: str

class ParentCreate(ParentBase):
    pass  # No extra fields needed for registration

class ParentResponse(ParentBase):
    id: int

    class Config:
        from_attributes = True

class ParentLogin(BaseModel):
    mobile: str
    otp: str
