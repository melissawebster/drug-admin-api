from pydantic import BaseModel


class DrugResponse(BaseModel, from_attributes=True):
    name: str
    price: float
    stock: int

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "name": "Piroxicam",
                "price": 20,
                "stock": "50"
            }
        }


class DrugCreate(BaseModel):
    name: str
    price: float
    stock: int

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "name": "Piroxicam",
                "price": 20,
                "stock": "50"
            }
        }