from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.requests import Request
from BSSAPI.api.models.data_models import CreateUptade
from common_modules.config import Config
from common_modules.logger import get_logger
from BSSAPI.app import rabbit
import json
import uuid

router = APIRouter()
logger = get_logger('NOTIFY_ROUTER')


@router.post("/update-task",
             summary="Запрос на обновление задачи",
             description="",
             status_code=202,
             tags=['task'])
async def update(data: CreateUptade, request: Request) -> JSONResponse:
    operation_id = uuid.uuid4()
    body = json.dumps(jsonable_encoder(data), ensure_ascii=False)
    await rabbit.send_message_async(Config.get('RABBIT', 'queue_notify'), body, operation_id)
    return JSONResponse(status_code=202, content={'message': 'success'})


