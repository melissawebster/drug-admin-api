from pydantic import BaseModel


class DrugResponse(BaseModel):
    name: str
    price: float
    stock: bool

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "name": "Piroxicam",
                "price": 20,
                "stock": True
            }
        }


class DrugCreate(BaseModel):
    name: str
    price: float
    stock: bool

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "name": "Vitex",
                "price": 30,
                "stock": True
            }
        }


class DrugUpdate(BaseModel):
    name: str
    price: float
    stock: bool

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "name": "Tandrilax",
                "price": 10,
                "stock": False
            }
        }