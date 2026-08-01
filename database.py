from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql://avnadmin:AVNS_sQndrfyDQ7y4GeN93ff@mysql-59bb94d-kavyaadivarapu08-4186.e.aivencloud.com:19919/defaultdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
