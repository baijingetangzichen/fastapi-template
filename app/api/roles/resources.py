import json
import asyncio

from fastapi import APIRouter, status, UploadFile, Request, Body, Depends, HTTPException
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi_pagination import pagination_ctx, Page
from fastapi_pagination.ext.async_sqlalchemy import paginate

from app.config import Config
from app.config.extend import current_logger, get_db
from app.common.utils import get_uuid, async_bulk_insert, DB_COMMIT_CODE, muti_async_bulk_insert
from app.common.req_res_parse import FormatJSONResponse
from app.common.pagination import Page, CustomPageParams


from .models import Role
from .schema import RoleSchema
from .tasks import add_together, pow_func
inner_router = APIRouter()

from celery import chain as celery_chain
@inner_router.get("/test")
async def add_node():
    data = {
        'code': 0,
        'message': '',
        'data': 'add role success'
    }
    add_together.delay(1, "2")
    batch_chain = celery_chain(add_together.s(1, "2"), pow_func.s(3))
    batch_chain.apply_async()
    # current_logger.info(dir(FormatJSONResponse))
    # return JsonResponse(content=data, status_code=status.HTTP_200_OK, name="aaa")
    return FormatJSONResponse(status_code=status.HTTP_200_OK)


@inner_router.post("/")
async def create_role(payload=Body(), session: AsyncSession=Depends(get_db)):
    name = payload.get("name")
    zh_name = payload.get("zh_name")
    role_objs = []
    for i in range(29500, 100000):
        role_objs.append({"id": get_uuid(), "name": f"{name}{i}", "zh_name": f"{zh_name}{i}"})
    commit_result = await muti_async_bulk_insert(Role, role_objs)
    if commit_result in DB_COMMIT_CODE:
        current_logger.error(f"提交数据库异常")
        return HTTPException(status_code=404, detail="提交数据库异常")
    return FormatJSONResponse(content=role_objs, status_code=status.HTTP_200_OK, name="role_list")


@inner_router.get("/", response_model=Page[RoleSchema], dependencies=[Depends(pagination_ctx(Page))])
async def get_roles(session: AsyncSession = Depends(get_db)):
    current_logger.info(dir(session))
    query = select(Role)
    querty_set = await paginate(session, query)
    current_logger.info(querty_set)
    return FormatJSONResponse(status_code=status.HTTP_200_OK, content=querty_set, name="role_list")

@inner_router.get("/{role_id}", response_model=RoleSchema)
async def get_role(role_id: str, session: AsyncSession = Depends(get_db)):
    query = select(Role).filter(Role.id == role_id)
    result = await session.execute(query)
    item = result.scalars().first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item = json.loads(RoleSchema(id=item.id, name=item.name, zh_name=item.zh_name).json())
    return FormatJSONResponse(status_code=status.HTTP_200_OK, content=item)


