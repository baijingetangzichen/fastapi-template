from __future__ import absolute_import

import os
from os import getenv
from kombu import Queue, Exchange

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 更多配置参数详见 https://docs.celeryq.dev/en/stable/userguide/configuration.html
# 命令详情 https://docs.celeryq.dev/en/latest/userguide/workers.html

# celery配置
BROKER_URL = os.getenv("BROKER_URL", "redis://172.16.2.10:35996/3")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://172.16.2.160:35996/5")
# 任务过期时间，celery任务执行结果的超时时间
CELERY_TASK_RESULT_EXPIRES = 24 * 60 * 60
# celery worker的并发数，默认是服务器的内核数目,也是命令行-c参数指定的数目
CELERYD_CONCURRENCY = getenv("CELERYD_CONCURRENCY", 2)
# celery worker每次去redis取任务的数量，默认值就是4
CELERYD_PREFETCH_MULTIPLIER = 4
# 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# 启动时区设置
CELERY_ENABLE_UTC = True
# 任务执行结果序列化方式
CELERY_RESULT_SERIALIZER = 'json'
# 任务的序列化方式
CELERY_TASK_SERIALIZER = 'json'
# 超时再分配时间
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# 手动注册任务
# CELERY_INCLUDE = ['apps.ann_task.tasks']
# 日志级别 DEBUG, INFO, WARNING, ERROR, or CRITICAL
CELERYD_REDIRECT_STDOUTS_LEVEL = getenv("CELERY_LOG_LEVEL", "INFO")
CELERYD_REDIRECT_STDOUTS = getenv("CELERYD_REDIRECT_STDOUTS", "Enabled")
CELERYD_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
CELERYD_TASK_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s [%(task_name)s(%(task_id)s)] %(message)s"
CELERY_DEFAULT_QUEUE = getenv("CELERY_DEFAULT_QUEUE", "ann-task-celery-queue")

# celery_default_exchange = Exchange("celery_default_exchange", durable=True, type='direct')
# ann_task_document_exchange = Exchange("ann_task_document_exchange", durable=True, type='direct')



# CELERY_QUEUES = (
#     Queue('celery_default_queue', exchange=celery_default_exchange, routing_key='celery_default_routing'),
#     Queue('ann_task_document_queue', exchange=ann_task_document_exchange, routing_key='ann_task_document_ies_routing'),
# )

# ANN_TASK_DOCUMENT_ROUTING = {'queue': 'ann_task_document_queue', 'routing_key': 'ann_task_document_routing'}


# CELERY_ROUTES = {
#     # 'apps.ann_task.tasks.document_task_smart_ann': ANN_TASK_DOCUMENT_ROUTING
# }

CELERY_DEFAULT_QUEUE = "celery_default_queue"
CELERY_DEFAULT_EXCHANGE = "celery_default_exchange"
CELERY_DEFAULT_ROUTING_KEY = "celery_default_routing"