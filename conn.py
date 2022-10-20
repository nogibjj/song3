from app.core.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = f"mysql://{settings.mysql_user}:{settings.mysql_password}@{settings.mysql_host}/{settings.mysql_db_name}?charset=utf8"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding='utf-8',
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()