from app.config.celery_object import celery_app
from loguru import logger
from app.config.extend import get_db, current_logger
from sqlalchemy.future import select
from app.api.roles.models import Role
import asyncio
from celery import Task
import uvloop


class AsyncTask(Task):
    def __call__(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.run(*args, **kwargs))
        # return asyncio.run(self.run(*args, **kwargs))


@celery_app.task(bind=True, name="add_together", base=AsyncTask)
async def add_together(self, a, b):
    current_logger.info(f"{int(a) + int(b)}")
    # logger.info(f"task属性: {dir(self)}")
    async for session in get_db():
        query = select(Role).filter(Role.id == "9c8ff5d62f7311efb38f60a44c243841")
        result = await session.execute(query)
        item = result.scalars().first()
        current_logger.info(f"角色中文名称{item.name}")
    return int(a) + int(b)

@celery_app.task(name="pow_func", base=AsyncTask)
async def pow_func(x, y):
    s = pow(x, y)
    current_logger.info(f"结果是 {s}")