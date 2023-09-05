from pydantic import BaseModel

class DrugSchema(BaseModel):
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