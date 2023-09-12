from pydantic import BaseModel


class DrugResponse(BaseModel):
    name: str
    price: float
    stock: int

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "name": "Piroxicam",
                "price": 20,
                "stock": 50
            }
        }


class DrugCreate(BaseModel):
    name: str
    price: float
    stock: int

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "name": "Vitex",
                "price": 30,
                "stock": 20
            }
        }