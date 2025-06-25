from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from app.schemas.cat import SpyCatCreate, SpyCatOut, SpyCatUpdate
from app.crud.cat import (
    create_spy_cat, get_all_cats, get_cat_by_id, update_cat_salary, delete_cat
)
from app.database import SessionLocal

router = APIRouter(prefix="/cats", tags=["Spy Cats"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=SpyCatOut)
def create_cat(cat: SpyCatCreate, db: Session = Depends(get_db)):
    return create_spy_cat(db, cat)

@router.get("", response_model=list[SpyCatOut])
def list_cats(db: Session = Depends(get_db)):
    return get_all_cats(db)

@router.get("/{cat_id}", response_model=SpyCatOut)
def get_cat(cat_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return get_cat_by_id(db, cat_id)

@router.put("/{cat_id}", response_model=SpyCatOut)
def update_salary(cat_id: int, update: SpyCatUpdate, db: Session = Depends(get_db)):
    return update_cat_salary(db, cat_id, update.salary)

@router.delete("/{cat_id}")
def remove_cat(cat_id: int, db: Session = Depends(get_db)):
    return delete_cat(db, cat_id)
