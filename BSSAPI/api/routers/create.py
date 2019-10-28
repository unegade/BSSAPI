from fastapi import APIRouter, Depends
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


@router.post("/create-task",
             summary="Запрос на создание задачи",
             description="",
             tags=['task'])
async def create(data: CreateUptade, request: Request) -> JSONResponse:
    operation_id = uuid.uuid4()
    body = json.dumps(jsonable_encoder(data), ensure_ascii=False)
    try:
        await rabbit.send_message_async(Config.get('RABBIT', 'queue_notify'), body, operation_id)
        response = JSONResponse(status_code=200, content={'message': 'success'})
    except Exception as ex:
        logger.error(ex)
        response = JSONResponse(status_code=500, content={'message': 'Ошибка на стороне сервера.'})
    return response


