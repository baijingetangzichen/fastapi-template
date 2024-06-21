from fastapi import APIRouter, status, UploadFile, Request, Body, Path, Query, WebSocket
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from app.config import Config
from app.config.extend import current_logger

inner_router = APIRouter()

@inner_router.get("/test")
def add_node():
    data = {
        'code': 0,
        'message': '',
        'data': 'add success'
    }
    current_logger.info("add node")
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)