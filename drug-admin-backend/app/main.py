from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:5173"]
)

@app.get("/")
def root():
    return {"message": "Drug Admin API"}

app.include_router(router)