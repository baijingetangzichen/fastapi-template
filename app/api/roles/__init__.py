from fastapi import APIRouter
from .resources import inner_router

role_router = APIRouter()
role_router.include_router(inner_router, tags=['role'], prefix='/role')