from sqlalchemy.orm import Session
from app.models.cat import SpyCat
from app.schemas.cat import SpyCatCreate

def create_spy_cat(db: Session, cat: SpyCatCreate):
    db_cat = SpyCat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def get_all_cats(db: Session):
    return db.query(SpyCat).all()

def get_cat_by_id(db: Session, cat_id: int):
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not cat:
        raise ValueError("Cat not found")
    return cat

def update_cat_salary(db: Session, cat_id: int, new_salary: float):
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not cat:
        raise ValueError("Cat not found")
    cat.salary = new_salary
    db.commit()
    db.refresh(cat)
    return cat

def delete_cat(db: Session, cat_id: int):
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not cat:
        raise ValueError("Cat not found")
    db.delete(cat)
    db.commit()
    return {"detail": "Cat deleted"}
