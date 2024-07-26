import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pro_dir = os.path.dirname(BASE_DIR)
if not os.path.exists(f"{pro_dir}/logs"):
    os.makedirs(f"{pro_dir}/logs")

def set_log_obj():
    import logging
    from concurrent_log_handler import ConcurrentRotatingFileHandler
    from app.config import Config
    level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'crit': logging.CRITICAL
        }
    set_log_level = Config.LOG_LEVEL
    logging.basicConfig(level=level_relations.get(set_log_level.lower()), datefmt='%Y-%m-%d %A %H:%M:%S')  # 调试debug级
    # 1. 日志输出到终端
    stream_handler = logging.StreamHandler(sys.stdout)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(asctime)s 进程ID - %(process)d 线程ID - [%(thread)d:%(threadName)s] - [%(filename)s:%(module)s:%(lineno)s:%(funcName)s] - [%(levelname)s]: %(message)s')
    stream_handler.setFormatter(formatter)
    logger_obj = logging.getLogger("fastapi_template")
    logger_obj.addHandler(stream_handler)
    file_log_handler = ConcurrentRotatingFileHandler(os.path.join(pro_dir, f"logs/{os.getenv('PROJECT_NAME', 'fastapi_template')}.log"), maxBytes=1024 * 1024 * 10, backupCount=100)
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logger_obj.addHandler(file_log_handler)
    # gun_logger_tuple = (logging.getLogger('uvicorn.error'), logging.getLogger('uvicorn.access'),
    #                     logging.getLogger('sqlalchemy.engine'), logging.getLogger("sqlalchemy.pool"),
    #                     logging.getLogger('gunicorn.error'), logging.getLogger('gunicorn.access'))
    # for logger in gun_logger_tuple:
    #     logger.setLevel(level=level_relations.get(Config.LOG_LEVEL))
    #     logger.addHandler(logger_obj)
    return logger_obj