from logging import DEBUG, INFO, ERROR, WARNING

LOGGER_LEVEL = INFO

FASTAPI_TITLE: str = 'Микросервис API для нотификаций из BSS'
FASTAPI_VERSION: str = '1.0'
FASTAPI_HOST: str = '0.0.0.0'
FASTAPI_PORT: int = 8000
FASTAPI_DEBUG: bool = False

RABBIT_URL: str = 'amqp://guest:guest@10.111.122.51:5672'
RABBIT_QUEUE_NOTIFY: str = 'notify'
