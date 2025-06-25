from sqlalchemy.orm import Session
from app.models.mission import Mission, Target
from app.models.cat import SpyCat
from app.schemas.mission import MissionCreate

def create_mission_with_targets(db: Session, mission: MissionCreate):
    if not (1 <= len(mission.targets) <= 3):
        raise ValueError("Mission must have between 1 and 3 targets")
    new_mission = Mission()
    db.add(new_mission)
    db.flush()
    for target in mission.targets:
        db_target = Target(mission_id=new_mission.id, **target.dict())
        db.add(db_target)
    db.commit()
    db.refresh(new_mission)
    return new_mission

def get_all_missions(db: Session):
    return db.query(Mission).all()

def get_mission_by_id(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise ValueError("Mission not found")
    return mission

def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not mission or not cat:
        raise ValueError("Mission or Cat not found")
    mission.cat_id = cat_id
    db.commit()
    return {"detail": f"Cat {cat_id} assigned to mission {mission_id}"}

def delete_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise ValueError("Mission not found")
    if mission.cat_id:
        raise ValueError("Mission is already assigned to a cat")
    db.query(Target).filter(Target.mission_id == mission_id).delete()
    db.delete(mission)
    db.commit()
    return {"detail": "Mission deleted"}
