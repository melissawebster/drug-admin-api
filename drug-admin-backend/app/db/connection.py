from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///app/db/database"

Engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=Engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()