
from fastapi import FastAPI
from common_modules.rabbit import Rabbit
from BSSAPI.api.routers import general, notify
from BSSAPI.settings import *
from BSSAPI.api.api_handlers import validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
import logging
import uvicorn

# Объявление глобальных переменных
app = FastAPI(title=FASTAPI_TITLE, version=FASTAPI_VERSION, description=FASTAPI_DESCRIPTION)
rabbit = Rabbit(RABBIT_URL, 'Notify')


def api_init():
    """
    Инициализация FASTAPI
    :return: None
    """
    app.include_router(notify.router)
    app.include_router(general.router)
    app.add_exception_handler(400, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)


if __name__ == "__main__":
    logging.basicConfig(level=LOGGER_LEVEL)
    api_init()
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT, debug=FASTAPI_DEBUG, log_level="info", reload=True)
