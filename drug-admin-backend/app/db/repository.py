#FastAPI
from fastapi import Depends

#SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import update

# Typing
from typing import List

#Database Imports
from .connection import get_db
from .models import Drug


def repo_get_all(db: Session = Depends(get_db)):
    return db.query(Drug).all()


def repo_get_by_name(name: str, db: Session = Depends(get_db)):
    if name == '':
        return repo_get_all(db)
    return db.query(Drug).filter(Drug.name.ilike(f"%{name}%")).all()


def repo_get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Drug).filter(Drug.id == id).one_or_none()


def repo_update(id: int, drug_update: dict, db: Session = Depends(get_db)):
    drug_to_update = db.query(Drug).filter(Drug.id == id).update(drug_update)
    if drug_to_update:
        db.commit()
        return True
    return False


def repo_delete_by_id(id: int, db: Session = Depends(get_db)):
    drug_to_delete =  db.query(Drug).filter(Drug.id == id).one_or_none()
    if drug_to_delete:
        db.delete(drug_to_delete)
        db.commit()
        return True
    return False
