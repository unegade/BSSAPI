from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from starlette.responses import Response, PlainTextResponse, JSONResponse
from starlette.requests import Request
from data_models import Notification
from logger import logger
import uvicorn
import settings
import json

app = FastAPI(title="Микросервис API для нотификаций из BSS", version="1.0")


@app.post("/notify",
          summary="Добавить данные",
          description="Функция добавляет данные")
def read_root(data: Notification, request: Request):
    logger.debug(f'REQUEST {request.client.host} {request.url.path}\nheaders={request.headers}\nbody={data.json()}')
    response = JSONResponse(status_code=200, content='success')
    logger.debug(f'RESPONSE {request.client.host} {request.url.path} {response.status_code}\nheaders={response.headers}\nbody={response.body}')
    return response


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     logger.debug(f'{request.client.host}')
#     response: Response = await call_next(request)
#     logger.debug(f'{response.status_code}')
#     return response


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc):
    logger.error(f'{request.client.host} {request.url} {str(exc)}')
    return PlainTextResponse(str(exc), status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, debug=True)