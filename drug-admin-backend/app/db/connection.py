from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///drugs-database.db"

Session = sessionmaker(bind=create_engine(DATABASE_URL))

Engine = create_engine(DATABASE_URL)