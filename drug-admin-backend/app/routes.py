#FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

#Database-related
from sqlalchemy.orm import Session
from .db.connection import get_db
from .db.models import Drug

#Repository
from .db.repository import repo_get_all
from .db.repository import repo_get_by_id

#Typing
from typing import Annotated
from typing import List


router = APIRouter(tags=['Drugs'])


@router.get('/drugs/{id}')
def get_by_id(id: int,
              db: Session = Depends(get_db)):
    """
    Gets a drug by id

    Args:
        id (int): the id to query

    Returns:
        A drug or none
    """
    result = repo_get_by_id(id, db)
    return result

@router.get('/drugs')
def get_all(name: Annotated [str | None, Query(max_lenght=50)] = None, 
              db: Session = Depends(get_db)):
    """
    Gets all drugs

    Args:
        name (str | None): the name to filter the search (optional)
        db (Session): the database session

    Returns:
        A list of drugs

    """    
    result = repo_get_all(name, db)
    return result

