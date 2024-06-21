from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class SharedStateMiddleware(BaseHTTPMiddleware):
    """
    共享接口中的有状态的变量
    """
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.shared_state = {}  # 定义一个字典，用于存储共享的数据

    async def dispatch(self, request: Request, call_next):
        # 设置共享状态
        request.state.shared = self.shared_state
        # 其他中间件或路由处理函数可以通过 request.state.shared 获得这一共享状态
        response = await call_next(request)
        return response