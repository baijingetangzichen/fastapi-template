from __future__ import annotations

import json

import math
from typing import TypeVar, Generic, Sequence

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from fastapi_pagination.utils import create_pydantic_model
from pydantic import BaseModel

T = TypeVar("T")


class CustomPageParams(BaseModel, AbstractParams):
    # 默认值，用户请求时可以变化
    page: int = Query(1, ge=1, description="Page number")
    # 默认值，用户请求时可以变化
    size: int = Query(20, gt=0, le=100, description="Page size")

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.size,
            offset=self.size * (self.page - 1),
        )


class Page(AbstractPage[T], Generic[T]):
    results: Sequence[T]
    total: int
    page: int
    size: int
    next: str
    previous: str
    total_pages: int

    __params_type__ = CustomPageParams  # Set params related to Page

    @classmethod
    def create(
            cls,
            results: results,
            total: int,
            params: CustomPageParams,
    ) -> Page[T]:
        page = params.page
        size = params.size
        total_pages = math.ceil(total / params.size)
        next = f"?page={page + 1}&size={size}" if (page + 1) <= total_pages else "null"
        previous = f"?page={page - 1}&size={size}" if (page - 1) >= 1 else "null"

        # return cls(results=results, total=total, page=params.page,
        #            size=params.size,
        #            next=next,
        #            previous=previous,
        #            total_pages=total_pages)
        schema_res = create_pydantic_model(cls, results=results, total=total, page=params.page,
                              size=params.size,
                              next=next,
                              previous=previous,
                              total_pages=total_pages)
        return json.loads(schema_res.json())