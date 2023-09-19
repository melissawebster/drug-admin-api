#Standard Imports
from sqlalchemy import select
from sqlalchemy.orm import Session
#from .connection import Session
from sqlalchemy.sql.expression import text

# Typing Imports
from typing import List

#Database Imports
from .connection import get_db
from .models import Drug



def repo_get_all(db: Session):
    return db.query(Drug).all()

def repo_get_by_name(name: str, db: Session):
    if not name:
        return repo_get_all(db)
    return db.query(Drug).filter(Drug.name.ilike(f"%{name}%")).all()

def repo_get_by_id(id: int, db: Session):
    return db.query(Drug).filter(Drug.id == id).one_or_none()
