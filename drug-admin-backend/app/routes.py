from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from typing import Annotated
from typing import List

from sqlalchemy.orm import Session
from.db.connection import get_db
from .db.models import Drug
from .db.repository import get_by_name

#Schemas and Service
from app.services import DrugService
from app.schemas import DrugResponse
from app.schemas import DrugCreate


router = APIRouter(tags=['Drugs'])
drug_service = DrugService()


@router.get('/drugs')
def get_drugs(name: Annotated [str | None, Query(max_lenght=50)] = None, 
              db: Session = Depends(get_db)):
    """
    Gets all drugs

    Args:
        name (str | None): the name to filter the search (optional)
        db (Session): the database session

    Returns:
        A list of drugs

    """    
    drugs = get_by_name(name, db)
    return drugs

