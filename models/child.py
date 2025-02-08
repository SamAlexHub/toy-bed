from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"))

    # Relationship with parent
    parent = relationship("Parent", back_populates="children")
