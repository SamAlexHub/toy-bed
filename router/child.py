from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.child import Child
from schemas.child import ChildCreate, ChildResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-child/", response_model=ChildResponse)
def add_child(child: ChildCreate, db: Session = Depends(get_db)):
    new_child = Child(name=child.name, age=child.age, parent_id=child.parent_id)
    db.add(new_child)
    db.commit()
    db.refresh(new_child)
    return new_child

@router.get("/children/{parent_id}", response_model=list[ChildResponse])
def get_children(parent_id: int, db: Session = Depends(get_db)):
    children = db.query(Child).filter(Child.parent_id == parent_id).all()
    if not children:
        raise HTTPException(status_code=404, detail="No children found for this parent")
    return children
