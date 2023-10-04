#FastAPI
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import Query

#Database-related
from sqlalchemy.orm import Session
from .db.connection import get_db

#Schemas and Services
from .schemas import DrugResponse
from .schemas import DrugUpdate
from .schemas import DrugCreate
from .services import DrugService

#Exceptions
from .utils.exceptions import ResourceNotFound

#Typing
from typing import Annotated


router = APIRouter(tags=['Drugs'])
services = DrugService()


@router.get('/drugs/')
def get_all(db: Session = Depends(get_db)):
    """
    Gets all drugs

    Args:
        db (Session): the database session

    Returns:
        A list of drugs

    """    
    get = services.get_all(db)
    return get

@router.get('/drugs/get_by_name/{name}')
def get_by_name(name: str="", 
                db: Session = Depends(get_db)):
    """
    Gets drugs by name.

    Args:
        name: the name to filter the search (optional)
        db (Session): the database session

    Returns:
        A list of drugs

    """    
    try:
        get = services.get_by_name(name, db)
        return get
    except ResourceNotFound:
        raise HTTPException(status_code=404, 
                            detail="Drug not found")

@router.get('/drugs/get_by_id/{id}')
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
    try:
        get = services.get_by_id(id, db)
        return get
    except ResourceNotFound:
        raise HTTPException(status_code=404, 
                            detail="Drug not found")

@router.post('/drugs/post')
def create(drug: DrugCreate,
           db: Session = Depends(get_db)):
    """
    Creates a drug

    Args:
        name (str): the drug name
        price (float): the drug price
        stock (bool): if drug is in stock
        db (Session): the database session
    """

    create = services.create(drug, db)
    return create

@router.patch('/drugs/update/{id}')
def update(id: int,
           drug: DrugUpdate,
           db: Session = Depends(get_db)):
    """
    Updates a drug

    Args:
        name (str): the drug name
        price (float): the drug price
        stock (bool): if drug is in stock
        db (Session): the database session
    """
    try:
        update = services.update(id, drug, db)
        return update
    except ResourceNotFound:
        raise HTTPException(status_code=404, 
                            detail="Drug not found")

@router.delete('/drugs/delete/{id}')
def delete_by_id(id: int,
                 db: Session = Depends(get_db)):
    """
    Deletes a drug

    Args:
        id (int): the id to delete
        db (Session): the database session

    """
    try:
        delete = services.delete(id, db)
        return delete
    except ResourceNotFound:
        raise HTTPException(status_code=404, 
                            detail="Drug not found")