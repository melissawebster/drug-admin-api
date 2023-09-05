from fastapi import APIRouter

#Schemas and Service
from app.services import DrugService
from app.schemas import DrugResponse
from app.schemas import DrugCreate


router = APIRouter(tags=['Drugs'])
drug_service = DrugService()

@router.post('/drug', response_model=DrugResponse, status_code=201)
async def create(payload: DrugCreate):
    """
    ## Creates a drug.

    ### Args:  
      >  payload (DrugCreate): The payload create model.

    ### Raises:  

    ### Returns:  
      >  DrugResponse: The response model.
    """
    return await drug_service.create(payload)


@router.get('/drug')
def get_all():
    return {"message": "all drugs"}