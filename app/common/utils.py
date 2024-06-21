import uuid
import time

from sqlalchemy.exc import OperationalError

from app.config.extend import AsyncSessionLocal, current_logger, get_db


DB_COMMIT_CODE = ["1001", "1002", "1003", "1004"]


def get_uuid():
    return uuid.uuid1().hex


async def comm_only_commit_option(session):
    try:
        await session.commit()
    except Exception as e:
        try:
            current_logger.error(f"数据库第一次提交失败，原因是 {e} 正在尝试二次提交")
            # 停止0.5秒后，再次提交
            time.sleep(0.5)
            await session.commit()
        except Exception as e:
            try:
                current_logger.error(f"数据库二次提交失败，原因是 {e} 尝试三次提交")
                await session.commit()
                return "1001"
            except OperationalError as o_r:
                try:
                    current_logger.error(f"数据库三次提交后提交失败 OperationalError，原因是 {o_r}")
                    await session.rollback()
                    return "1002"
                except Exception as e:
                    current_logger.error(f"数据库三次提交后回滚失败，原因是 {e}")
                    return "1002"
            except Exception as e:
                current_logger.error(f"数据库三次提交后提交失败 Exception ，原因是 {e}")
                return "1002"


# 批量插入数据库
async def async_bulk_insert(model_obj, model_data):
    async with AsyncSessionLocal() as session:
        # 构造一个INSERT语句
        query = model_obj.__table__.insert().values(model_data)
        # 异步执行
        await session.execute(query)
        await session.commit()

# 批量插入数据库(多次提交)
async def muti_async_bulk_insert(model_obj, model_data):
    num = 0
    async for session in get_db():
        num += 1
        # 构造一个INSERT语句
        query = model_obj.__table__.insert().values(model_data)
        # 异步执行
        await session.execute(query)
        commmit_result = await comm_only_commit_option(session)
        current_logger.info(f"获取session次数 {num}")
        return commmit_result