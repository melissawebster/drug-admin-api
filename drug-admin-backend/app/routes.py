from fastapi import APIRouter, Depends, Query
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


@router.get('/drug')
def get_drugs(name: str = Query(None, alias="drug_name"), db: Session = Depends(get_db)):    
    drugs = get_by_name(name, db)
    return drugs

