from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.mission import MissionCreate, MissionOut
from app.crud.mission import (
    create_mission_with_targets,
    get_all_missions,
    get_mission_by_id,
    assign_cat_to_mission,
    delete_mission
)
from app.database import SessionLocal

router = APIRouter(prefix="/missions", tags=["Missions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=MissionOut)
def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    return create_mission_with_targets(db, mission)

@router.get("", response_model=list[MissionOut])
def list_missions(db: Session = Depends(get_db)):
    return get_all_missions(db)

@router.get("/{mission_id}", response_model=MissionOut)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    return get_mission_by_id(db, mission_id)

@router.put("/{mission_id}/assign/{cat_id}")
def assign_mission(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    return assign_cat_to_mission(db, mission_id, cat_id)

@router.delete("/{mission_id}")
def remove_mission(mission_id: int, db: Session = Depends(get_db)):
    return delete_mission(db, mission_id)
