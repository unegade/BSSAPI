from common_modules.config import Config
from fastapi import FastAPI
from common_modules.rabbit import Rabbit, RabbitSendException
from BSSAPI.api.api_handlers import validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
import uvicorn
import logging

Config.init('config.ini', 'config_dev.ini', API='BSS_API_', RABBIT='BSS_RABBIT_')

# Объявление глобальных переменных
app = FastAPI(title=Config.get('API', 'title'),
              version=Config.get('API', 'version'),
              description=Config.get('API', 'description'))
rabbit = Rabbit(url=Config.get('RABBIT', 'url'),
                connection_name=Config.get('DEFAULT', 'app_name'))

from BSSAPI.api.routers import index, notify, create, update

def api_init():
    """
    Инициализация FASTAPI
    :return: None
    """
    app.include_router(notify.router)
    app.include_router(create.router)
    app.include_router(update.router)
    app.include_router(index.router)
    app.add_exception_handler(400, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(RabbitSendException, validation_exception_handler)


def rabbit_init():
    rabbit.declare_queue(Config.get('RABBIT', 'queue_notify'))
    rabbit.declare_queue(Config.get('RABBIT', 'queue_create'))
    rabbit.declare_queue(Config.get('RABBIT', 'queue_update'))


if __name__ == "__main__":
    logger_level = logging.DEBUG if Config.get('DEFAULT', 'log_level') == 'debug' else logging.INFO
    logging.basicConfig(level=logger_level)
    api_init()
    rabbit_init()
    rabbit.loop_forever()
    uvicorn.run(app,
                host=Config.get('API', 'host'),
                port=Config.getint('API', 'port'),
                debug=Config.getboolean('API', 'debug'),
                log_level=Config.get('DEFAULT', 'log_level'))
