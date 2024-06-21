from fastapi import APIRouter
from .resources import inner_router
# from .models import *

user_router = APIRouter()

# tags 显示在 Swagger 上的标题
user_router.include_router(inner_router, tags=['users'], prefix='/user')