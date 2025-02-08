from pydantic import BaseModel

class ChildBase(BaseModel):
    name: str
    age: int

class ChildCreate(ChildBase):
    parent_id: int

class ChildResponse(ChildBase):
    id: int

    class Config:
        from_attributes = True
