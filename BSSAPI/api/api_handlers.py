from BSSAPI.app import app
from fastapi.exceptions import RequestValidationError
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from starlette.responses import Response
from BSSAPI.logger import logger



@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc):
    logger.error(f'{request.client.host} {request.url} {str(exc)}')
    return PlainTextResponse(str(exc), status_code=500)

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     logger.debug(f'{request.client.host}')
#     response: Response = await call_next(request)
#     logger.debug(f'{response.status_code}')
#     return response