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


def get_all(db: Session):
    return db.query(Drug).all()


def get_by_name(name: str, db: Session):
    if not name:
        return get_all(db)
    return db.query(Drug).filter(Drug.name.ilike(f"%{name}%")).all()