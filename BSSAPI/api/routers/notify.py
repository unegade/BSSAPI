from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.encoders import jsonable_encoder
from BSSAPI.api.models.data_models import Notification
from BSSAPI.logger import logger
from BSSAPI.app import rabbit_sender
from BSSAPI.settings import RABBIT_QUEUE_NOTIFY


router = APIRouter()


@router.post("/notify",
             summary="Добавить данные",
             description="Функция добавляет данные", tags=['notify'])
def read_root(data: Notification, request: Request):
    logger.debug(f'REQUEST {request.client.host} {request.url.path}\n\theaders={request.headers}\n\tbody={jsonable_encoder(data)}')
    try:
    # rabbit_sender.connect(RABBIT_QUEUE_NOTIFY)
    # rabbit_sender.send_message('notify','test')
    # a = rabbit_sender.get_channel()
    # rabbit_sender.send_message(RABBIT_QUEUE_NOTIFY, jsonable_encoder(data))
        response = JSONResponse(status_code=200, content='success')
    except Exception as ex:
        print(ex)
        response = JSONResponse(status_code=500, content='Ошибка на стороне сервера.')
    logger.debug(
        f'RESPONSE {request.client.host} {request.url.path} {response.status_code}\n\theaders={response.headers}\n\tbody={response.body.decode("utf-8")}')
    return response
