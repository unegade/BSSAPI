from starlette.responses import PlainTextResponse, JSONResponse
from starlette.requests import Request
from common_modules.logger import get_logger



logger = get_logger(__name__)
def validation_exception_handler(request: Request, exc):
    """
    Обработчик ошибки валидации.
    Добавляет логирование.
    """
    logger.error(f'{request.client.host} {request.url} 500 {str(exc)}')
    return PlainTextResponse(str(exc), status_code=500)


def http_exception_handler(request: Request, exc):
    """
    Обработчик HTTP ошибок.
    Добавляет логирование.
    """
    logger.error(f'{request.client.host} {request.url} {exc.status_code} {str(exc.detail)}')
    return PlainTextResponse('Ошибка на стороне сервера', status_code=500)
