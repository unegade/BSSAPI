from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.requests import Request
from BSSAPI.api.models.data_models import CreateUptade
from common_modules.logger import get_logger
from BSSAPI.app import rabbit
from BSSAPI.settings import RABBIT_QUEUE_UPDATE
import json
import uuid

router = APIRouter()
logger = get_logger('NOTIFY_ROUTER')


@router.post("/update-task",
             summary="Запрос на обновление задачи",
             description="",
             tags=['task'])
async def update(data: CreateUptade, request: Request) -> JSONResponse:
    operation_id = uuid.uuid4()
    body = json.dumps(jsonable_encoder(data), ensure_ascii=False)
    logger.debug(
        f'{operation_id} RQ {request.client.host} {request.url.path}\n\theaders={request.headers}\n\tbody={body}')
    try:
        await rabbit.send_message_async(RABBIT_QUEUE_UPDATE, body, operation_id)
        response = JSONResponse(status_code=200, content={'message': 'success'})
    except Exception as ex:
        logger.error(ex)
        response = JSONResponse(status_code=500, content={'message': 'Ошибка на стороне сервера.'})
    logger.debug(
        f'{operation_id} RS {request.client.host} {request.url.path} {response.status_code}\n\theaders={response.headers}\n\tbody={response.body.decode("utf-8")}')
    return response


