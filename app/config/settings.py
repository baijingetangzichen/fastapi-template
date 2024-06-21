import sys
from os import getenv
from os.path import dirname, abspath, join
from urllib.parse import quote_plus as urlquote

from .sd_config import ProxyConfig


class Config(ProxyConfig):
    APP_HOST = getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(getenv("APP_PORT", 32345))
    APP_RELOAD = getenv("APP_RELOAD", "False") == "True"
    project_dir = dirname(dirname(abspath(dirname(__file__))))
    STATIC_DIR = join(project_dir, 'static')
    LOG_LEVEL = getenv("LOG_LEVEL", "info")
    FASTAPI_PREFIX = getenv("DEMO_API_PREFIX", "/fastapi-prefix")
    # 数据库配置
    # db类型 mysql postgresql
    DB_TYPE = getenv("DB_TYPE", "postgresql")
    DB_USER = getenv("DB_USER", "comm_llm_api")
    DB_PASS = getenv("DB_PASS", "q8x06B4uF9JJ8B1Jh7xo")
    DB_HOST = getenv("DB_HOST", "172.16.2.13")
    DB_PORT = getenv("DB_PORT", "23432")
    DB_NAME = getenv("DB_NAME", "comm_llm_api")
    DB_SERVER = f"{DB_HOST}:{DB_PORT}"
    # 判断数据库是否需要ssl验证
    DB_SSL_DISABLE = getenv("DB_SSL_DISABLE", "False") == "True"
    # mysql
    if DB_TYPE == "mysql":
        # 数据库连接格式
        DRIVER = "aiomysql"
        SQLALCHEMY_DATABASE_URI = f"{DB_TYPE}+{DRIVER}://{DB_USER}:{urlquote(DB_PASS)}@{DB_SERVER}/{DB_NAME}"
    # postgresql
    elif DB_TYPE == "postgresql":
        DRIVER = 'asyncpg'
        SQLALCHEMY_DATABASE_URI = f"{DB_TYPE}+{DRIVER}://{DB_USER}:{urlquote(DB_PASS)}@{DB_SERVER}/{DB_NAME}"
        print("SQLALCHEMY_DATABASE_URI", SQLALCHEMY_DATABASE_URI)
    else:
        sys.exit(1)
