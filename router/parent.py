from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
import random
from database.database import SessionLocal
from models.parent import Parent
from schemas.parent import ParentCreate, ParentResponse, ParentLogin

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register/", response_model=ParentResponse)
def register_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    existing_parent = db.query(Parent).filter(Parent.mobile == parent.mobile).first()
    if existing_parent:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Mobile number already registered")
    
    new_parent = Parent(name=parent.name, mobile=parent.mobile)
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)
    return new_parent

@router.post("/send-otp/")
def send_otp(mobile: str, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.mobile == mobile).first()
    if not parent:
        raise HTTPException(status_code=404, detail="Parent not found")

    otp = str(random.randint(100000, 999999))
    parent.otp = otp
    db.commit()

    return {"message": "OTP sent successfully", "otp": otp}  # In production, send via SMS

@router.post("/login/")
def login_parent(login_data: ParentLogin, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.mobile == login_data.mobile, Parent.otp == login_data.otp).first()
    if not parent:
        raise HTTPException(status_code=401, detail="Invalid OTP")

    return {"message": "Login successful", "parent_id": parent.id}
