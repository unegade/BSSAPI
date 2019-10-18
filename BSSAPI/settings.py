from logging import DEBUG, INFO, ERROR, WARNING

LOGGER_LEVEL = DEBUG
# Настройки Web сервиса
FASTAPI_TITLE: str = 'Микросервис API для нотификаций из BSS'
FASTAPI_VERSION: str = '1.0'
FASTAPI_DESCRIPTION: str = '<a href="/docs">Еще документация по REST API</a>'
FASTAPI_HOST: str = '0.0.0.0'
FASTAPI_PORT: int = 8000
FASTAPI_DEBUG: bool = True if LOGGER_LEVEL == DEBUG else False
# Настройки подключения к RabbitMQ
RABBIT_URL: str = 'amqp://guest:guest@10.111.122.51:5672'
RABBIT_QUEUE_NOTIFY: str = 'notify'

