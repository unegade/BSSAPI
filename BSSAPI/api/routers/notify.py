from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.encoders import jsonable_encoder
from BSSAPI.api.models.data_models import Notification
from BSSAPI.logger import get_logger
from BSSAPI.app import rabbit
from BSSAPI.settings import RABBIT_QUEUE_NOTIFY
import json
from fastapi import HTTPException

router = APIRouter()
logger = get_logger(__name__)

@router.post("/notify",
             summary="Добавить данные",
             description="Функция добавляет данные", tags=['notify'])
async def read_root(data: Notification, request: Request):
    logger.debug(f'RQ {request.client.host} {request.url.path}\n\theaders={request.headers}\n\tbody={jsonable_encoder(data)}')
    body = json.dumps(jsonable_encoder(data), ensure_ascii=False)

    try:
        # await rabbit._send_message(RABBIT_QUEUE_NOTIFY, body)
        response = JSONResponse(status_code=200, content='success')
    except Exception as ex:
        logger.error(ex)
        raise HTTPException(status_code=500, detail="Ошибка на стороне сервера.")
    logger.debug(
        f'RS {request.client.host} {request.url.path} {response.status_code}\n\theaders={response.headers}\n\tbody={response.body.decode("utf-8")}')
    return JSONResponse(status_code=200, content='success')
