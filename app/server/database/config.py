from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# Database URL
URL_DATABASE = 'postgresql://postgres:Sandhra11$@localhost:5432/TimeTAB'

# SQLAlchemy engine and session
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()