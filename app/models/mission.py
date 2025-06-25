from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Mission(Base):
    __tablename__ = "missions"
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("spy_cats.id"), nullable=True)
    is_complete = Column(Boolean, default=False)
    cat = relationship("SpyCat", back_populates="missions")
    targets = relationship("Target", back_populates="mission")

class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, default="")
    is_complete = Column(Boolean, default=False)
    mission = relationship("Mission", back_populates="targets")
