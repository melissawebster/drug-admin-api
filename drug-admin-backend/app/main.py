from fastapi import FastAPI 
from app.routes import router

app = FastAPI() 

@app.get("/")
def root():
    return {"message": "Drug Admin API"}

app.include_router(router)