#FastAPI
from fastapi import Depends
from fastapi import Query

# Database-related
from app.db.models import Drug
import app.db.repository as repo
from .db.connection import get_db
from sqlalchemy.orm import Session

#Repository
from .db.repository import repo_get_all_by_name
from .db.repository import repo_get_by_id
from .db.repository import repo_delete_by_id
from .db.repository import repo_update

# Schemas
from app.schemas import DrugCreate
from app.schemas import DrugResponse
from app.schemas import DrugUpdate

#Typing
from typing import List
from typing import Annotated


class DrugService:

    def create(self, 
               drug: DrugCreate,
               db: Session = Depends(get_db)) -> DrugResponse:
        
        drug_to_create = Drug(
        **drug.model_dump()
        )

        db.add(drug_to_create)
        db.commit()

        return DrugResponse.model_validate(drug_to_create)


    def update(self, 
               id: int,
               drug: DrugUpdate,
               db: Session = Depends(get_db)) -> DrugResponse:
        
        drug_update = drug.model_dump()

        result = repo_update(id, drug_update, db)
        if result == True:
            return DrugResponse.model_validate(drug)
        

    def get_by_id(self,
                  id: int,
                  db: Session = Depends(get_db)) -> DrugResponse:
        
        result = repo_get_by_id(id, db)
        return result
    

    def get_all(self,
                name: Annotated [str | None, Query(max_lenght=50)] = None, 
                db: Session = Depends(get_db)) -> List[DrugResponse]:
        
        result = repo_get_all_by_name(name, db)
        return result
    

    def delete(self,
               id: int,
               db: Session = Depends(get_db)) -> DrugResponse:
        
        result = repo_delete_by_id(id, db)
        return result