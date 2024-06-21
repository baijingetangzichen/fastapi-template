import os
import sys
import logging

import loguru
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

current_dir = os.path.dirname(os.path.abspath(__file__))
pro_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(current_dir)
sys.path.append(pro_base_dir)

from app.config import Config, SharedStateMiddleware, set_log_obj
from app.api.users import user_router
from app.api.roles import role_router

app = FastAPI(title="FastAPI结构示例",  # 文档标题
        description="使用 FastAPI 实现 web后端 基础功能. 🚀",  # 文档简介
        version="0.0.1",  # 文档版本号
        docs_url=f"{Config.FASTAPI_PREFIX}/docs", redoc_url=None,
        openapi_url=f"{Config.FASTAPI_PREFIX}/openapi.json"
        )
app.add_middleware(SharedStateMiddleware)
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=['HEAD, OPTIONS, GET, POST, DELETE, PUT'],
                   allow_headers=['Content-Type, Content-Length, Authorization, Accept, X-Requested-With'],
                   max_age=86400
                   )
app.include_router(user_router, prefix=f"{Config.FASTAPI_PREFIX}")
app.include_router(role_router, prefix=f"{Config.FASTAPI_PREFIX}")

loguru.logger.info(app.routes)
add_pagination(app)
if __name__ == "__main__":

    logging.root.setLevel(logging.DEBUG)
    logging.info("Starting on  %s:%d ", Config.APP_HOST, Config.APP_PORT)

    # main:app main下面的 app，相当于注入
    # main: main.py 文件(也可理解为Python模块).
    # app: main.py 中 app = FastAPI()
    # 语句创建的app对象.
    # --reload: 在代码改变后重启服务器，只能在开发的时候使用
    uvicorn.run(app, host=Config.APP_HOST, port=Config.APP_PORT, reload=Config.APP_RELOAD, log_level=logging.DEBUG)
