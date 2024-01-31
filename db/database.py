import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_async_engine(DATABASE_URL)
DBSession = async_sessionmaker(autoflush=False, bind=engine)
session_maker = async_sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()