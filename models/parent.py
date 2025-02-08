from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    mobile = Column(String(15), unique=True, index=True, nullable=False)
    otp = Column(String(6), nullable=True)  # OTP for login

    # Relationship with children
    children = relationship("Child", back_populates="parent")
