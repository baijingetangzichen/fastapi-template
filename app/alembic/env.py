import os
import sys
import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from alembic import context

current_dir = os.path.dirname(os.path.abspath(__file__))
pro_base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("项目根目录", pro_base_dir)
sys.path.append(current_dir)
sys.path.append(pro_base_dir)

# 从你的模型或基础配置文件导入metadata
# 假设你的模型的元数据称为Base
from app.config.extend import Base
from app.config import Config
from app.api.users.models import *
from app.api.roles.models import *

TARGET_METADATA = Base.metadata

# 异步数据库URL配置
ASYNC_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

# 创建异步的数据库引擎
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)


# Alembic配置没有直接支持异步，我们需要做一些工作来适配
def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=TARGET_METADATA,

        # 如果模型使用了schema，则需显式声明
        # schema_translate_map={None: "your_schema"},
    )

    with context.begin_transaction():
        context.run_migrations()


# 新增一个异步的运行迁移的函数
async def run_migrations_online():
    # 将engine包裹在AsyncEngine中以确保是异步的
    async with async_engine.begin() as connection:
        # 运行前面定义的同步迁移函数
        await connection.run_sync(do_run_migrations)


# Alembic的env.py脚本入口点
if context.is_offline_mode():
    raise Exception("Alembic不支持该异步环境下的离线模式迁移")
else:
    asyncio.run(run_migrations_online())