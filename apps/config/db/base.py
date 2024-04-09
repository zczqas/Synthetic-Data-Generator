from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from apps.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(settings.ASYNC_SQLALCHEMY_DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


class Base(DeclarativeBase):
    pass
