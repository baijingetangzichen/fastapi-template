import json
import httpx
import typing
from fastapi.responses import Response, JSONResponse
from starlette.background import BackgroundTask

async def fetch_data(url: str, headers: dict = None, params: dict = None) -> json:
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        return response


class APIStatusConstant(object):
    """
    接口返回状态字段常量
    """

    # 成功的操作
    SUCCESS = "success"
    # 失败的操作
    ERROR = "error"
    # 未授权，一般在令牌验证失败时使用
    UNAUTHORIZED = "unauthorized"


class FormatJSONResponse(Response):
    media_type = "application/json"
    def __init__(
            self,
            content: typing.Any | None = None,
            status_code: int = 200,
            headers: typing.Mapping[str, str] | None = None,
            media_type: str | None = None,
            background: BackgroundTask | None = None,
            status: str = APIStatusConstant.SUCCESS,
            message: str | None = None,
            name: str = "data"
    ) -> None:
        # super().__init__(content, status_code, headers, media_type, background)
        self.status = status
        self.message = message
        self.status_code = status_code
        self.name = name
        if media_type is not None:
            self.media_type = media_type
        self.background = background
        self.body = self.render(content)
        self.init_headers(headers)

    def render(self, content: typing.Any) -> bytes:
        base = {"status_code": self.status_code, "status": self.status}
        if content:
            base.update({self.name: content})
        if self.message:
            base.update({"message": self.message})
        data = json.dumps(
            base,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")
        return data
