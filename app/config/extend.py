# 服务扩展
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import Config
from app.config import set_log_obj

current_logger = set_log_obj()
# from sqlalchemy.pool import QueuePool
# create_engine() 默认为使用 QueuePool 大小为5
# 参数 echo：打印执行日志，future：使用2.0新特性

async_engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI,
                                   echo=True,
                                   future=True,
                                   pool_size = 10,
                                   max_overflow = 10,
                                    pool_timeout = 60,
                                    pool_recycle = 3600
                                   )

# current_logger.info(dir(async_engine))

AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as async_session:
        yield async_session

