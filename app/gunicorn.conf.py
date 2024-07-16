#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import asyncio
import multiprocessing

from read_resource import get_cpu_quota_within_docker

# 根目录
chdir = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists("logs"):
    os.mkdir("logs")
# 预加载资源
preload_app = True
project_server_port = os.getenv("PROJECT_SERVER_PORT", "32345")

# 监听本机的端口
bind = f"0.0.0.0:{project_server_port}"
# 未决连接的最大数量，即等待服务的客户的数量
backlog = 2048

# 进程数 = cup数量 * 2 + 1
docker_cpus = get_cpu_quota_within_docker()
workers = (docker_cpus if docker_cpus else multiprocessing.cpu_count()) * 2 + 1
# if workers > 8:
#     workers = 8
# else:
#     workers = workers
# 线程数 = cup数量 * 2
threads = (docker_cpus if docker_cpus else multiprocessing.cpu_count()) * 2
# if threads > 2:
#     threads = 2
# else:
#     threads = threads
# if os.getenv("FLASK_CONFIG") == "dev":
#     workers = 2
#     threads = 2
# 工作模式为
workers = 2
threads = 2
worker_class = 'uvicorn.workers.UvicornWorker'

# 最大客户客户端并发数量,对使用线程和协程的worker的工作有影响
# 服务器配置设置的值  1200：中小型项目  上万并发： 中大型
# 服务器硬件：宽带+数据库+内存
# 服务器的架构：集群 主从
worker_connections = 1200
# 超时 默认30秒
timeout = 120
# 连接上等待请求的秒数，默认情况下值为2
keepalive = 2

# 进程名称
proc_name = os.getenv("PROJECT_NAME", "llm-sd-api")
# 进程pid记录文件
pidfile = 'gunicorn.pid'
# 日志等级
loglevel = 'debug'
# 日志文件名
logfile = './logs/debug.log'
# 访问记录
accesslog = './logs/access.log'
# 访问记录格式
# access_log_format = '%(h)s %(t)s %(U)s %(q)s'
x_forwarded_for_header = "X-Real-IP"
# access_log_format = '%({X-Real-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
access_log_format = '%({X-Real-IP}i)s %(h)s %(t)s %(l)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# 日志格式
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        "gunicorn.error": {
            "level": "DEBUG",  # 打日志的等级可以换的，下面的同理
            "handlers": ["error_file"],  # 对应下面的键
            "propagate": 1,
            "qualname": "gunicorn.error"
        },

        "gunicorn.access": {
            "level": "DEBUG",
            "handlers": ["access_file"],
            "propagate": 0,
            "qualname": "gunicorn.access"
        }
    },
    'handlers': {
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 1024,  # 打日志的大小，我这种写法是1个G
            "backupCount": 1,  # 备份多少份，经过测试，最少也要写1，不然控制不住大小
            "formatter": "generic",  # 对应下面的键
            # 'mode': 'w+',
            "filename": "error.log"  # 打日志的路径
        },
        "access_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 1,
            "formatter": "generic",
            "filename": "access.log",
        }
    },
    'formatters': {
        "generic": {
            "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'",  # 打日志的格式
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",  # 时间显示方法
            "class": "logging.Formatter"
        },
        "access": {
            "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'",
            "class": "logging.Formatter"
        }
    }
}

