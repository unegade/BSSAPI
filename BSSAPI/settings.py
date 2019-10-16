from logging import DEBUG, INFO, ERROR, WARNING

LOGGER_LEVEL = DEBUG

FASTAPI_TITLE: str = 'Микросервис API для нотификаций из BSS'
FASTAPI_VERSION: str = '1.0'
FASTAPI_HOST: str = '0.0.0.0'
FASTAPI_PORT: int = 8000
FASTAPI_DEBUG: bool = False

RABBIT_HOST: str = '10.111.122.51'
RABBIT_PORT: int = 5672
RABBIT_USER: str = 'guest'
RABBIT_PASS: str = 'guest'
RABBIT_QUEUE_NOTIFY: str = 'notify'
