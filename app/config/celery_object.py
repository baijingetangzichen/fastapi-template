import os
import logging
from celery import Celery
# from celery.signals import setup_logging
from app.config import celery_conf
from logging.handlers import TimedRotatingFileHandler
from concurrent_log_handler import ConcurrentRotatingFileHandler
from logging.config import dictConfig

celery_app = Celery(os.getenv("PROJECT_NAME", "fastapi-template"))
# celery_app.config_from_object("app.config.celery_conf")
celery_app.config_from_object(celery_conf)

celery_app.autodiscover_tasks(['app.api.roles.tasks'])
# LOG_CONFIG = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             # 'datefmt': '%m-%d-%Y %H:%M:%S'
#             'format': '%(asctime)s \"%(pathname)s：%(module)s:%(funcName)s:%(lineno)d\" [%(levelname)s]- %(message)s'
#         }
#     },
#     'handlers': {
#         'celery': {
#             # 'level': 'INFO',
#             # 'class': 'logging.handlers.RotatingFileHandler',
#             'level': 'DEBUG',
#             'formatter': 'simple',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'your_name.log',
#             'when': 'midnight',
#             'encoding': 'utf-8',
#         },
#     },
#     'loggers': {
#          'myapp': {
#             'handlers': ['celery'],
#             'level': 'INFO',
#             'propagate': True,
#          }
#     }
# }
#
# def setup_logging(**kwargs):
#     dictConfig(LOG_CONFIG)
#
# celery_app.user_options['preload'].add(setup_logging)


