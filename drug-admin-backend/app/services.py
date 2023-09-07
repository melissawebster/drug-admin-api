#Schemas
from app.schemas import DrugCreate
from app.schemas import DrugResponse

#Models
from app.db.models import Drug

class DrugService:

    async def create(self, drug_create: DrugCreate) -> DrugResponse:
        """
        Creates a drug.

        Args:
            drug_create (DrugCreate): The drug creation model.

        Returns:  
            DrugResponse: The response model.
        """

        drug_to_create = Drug(
            **drug_create.model_dump()
        )

        return DrugResponse.model_validate(drug_to_create)