import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.getenv("POSTGRES_USER", "admin")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "SuperXavfsizParol123!")
DB_NAME = os.getenv("POSTGRES_DB", "main_db")
HOST = os.getenv("POSTGRES_HOST", "postgres_db")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
