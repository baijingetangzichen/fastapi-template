import os
import sys
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler
from celery.utils.log import get_task_logger
# from celery.utils.log import get_logger
logger = get_task_logger("celery_task_log")

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


