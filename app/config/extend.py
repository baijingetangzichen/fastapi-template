# 服务扩展
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import Config
from app.config import set_log_obj

async_engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as async_session:
        yield async_session

current_logger = set_log_obj()