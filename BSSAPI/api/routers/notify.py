from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.requests import Request
from BSSAPI.api.models.data_models import Notification
from common_modules.config import Config
from common_modules.logger import get_logger
from BSSAPI.app import rabbit
import json
import uuid

router = APIRouter()
logger = get_logger('NOTIFY_ROUTER')


@router.post("/notifcationAssigneeUser",
             summary="Нотификация с результатом назначения",
             description="Этот сценарий используется для случаев, когда нужно назначить задачу с одного исполнителя "
                         "на другого исполнителя",
             tags=['notifcationAssigneeUser'])
async def notify(data: Notification) -> JSONResponse:
    operation_id = uuid.uuid4()
    body = json.dumps(jsonable_encoder(data), ensure_ascii=False)
    await rabbit.send_message_async(Config.get('RABBIT', 'queue_notify'), body, operation_id)
    return JSONResponse(status_code=200, content={'message': 'success'})


