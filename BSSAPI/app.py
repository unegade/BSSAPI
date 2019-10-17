from fastapi import FastAPI
from BSSAPI.queue_manager.rabbit import Rabbit
from BSSAPI.api.routers import general, notify
from BSSAPI.settings import *
from BSSAPI.api.api_handlers import validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException
import uvicorn

app = FastAPI(title=FASTAPI_TITLE, version=FASTAPI_VERSION)
rabbit = Rabbit(RABBIT_URL)


def api_init():
    app.include_router(notify.router)
    app.include_router(general.router)
    app.add_exception_handler(400, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    rabbit.connect()

if __name__ == "__main__":
    api_init()
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT, debug=FASTAPI_DEBUG)
