#FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

#Database-related
from sqlalchemy.orm import Session
from .db.connection import get_db
from .db.models import Drug

#Repository
from .db.repository import repo_get_all_by_name
from .db.repository import repo_get_by_id
from .db.repository import repo_delete_by_id
from .db.repository import repo_update

#Schemas
from .schemas import DrugResponse
from .schemas import DrugUpdate
from .schemas import DrugCreate

#Typing
from typing import Annotated
from typing import List


router = APIRouter(tags=['Drugs'])


@router.post('/drugs')
def create(drug: DrugCreate,
           db: Session = Depends(get_db)) -> DrugResponse:
    """
    Creates a drug

    Args:
        name (str): the drug name
        price (float): the drug price
        stock (bool): if drug is in stock
        db (Session): the database session
    """
    drug_to_create = Drug(
        **drug.model_dump()
    )

    db.add(drug_to_create)
    db.commit()

    return DrugResponse.model_validate(drug_to_create)


@router.patch('/drugs/{id}')
def update(id: int,
           drug: DrugUpdate,
           db: Session = Depends(get_db)) -> DrugResponse:
    """
    Updates a drug

    Args:
        name (str): the drug name
        price (float): the drug price
        stock (bool): if drug is in stock
        db (Session): the database session
    """
    drug_update = drug.model_dump()

    result = repo_update(id, drug_update, db)
    if result == True:
        return DrugResponse.model_validate(drug)


@router.get('/drugs/{id}')
def get_by_id(id: int,
              db: Session = Depends(get_db)):
    """
    Gets a drug by id

    Args:
        id (int): the id to query
        db (Session): the database session

    Returns:
        A drug or none
    """
    result = repo_get_by_id(id, db)
    return result


@router.get('/drugs')
def get_all_by_name(name: Annotated [str | None, Query(max_lenght=50)] = None, 
              db: Session = Depends(get_db)):
    """
    Gets all drugs

    Args:
        name (str | None): the name to filter the search (optional)
        db (Session): the database session

    Returns:
        A list of drugs

    """    
    result = repo_get_all_by_name(name, db)
    return result


@router.delete('/drugs/{id}')
def delete_by_id(id: int,
                 db: Session = Depends(get_db)):
    """
    Deletes a drug

    Args:
        id (int): the id to delete
        db (Session): the database session

    """
    result = repo_delete_by_id(id, db)
    return result