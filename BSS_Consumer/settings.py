from logging import DEBUG, INFO, ERROR, WARNING

LOGGER_LEVEL = DEBUG

# Настройки подключения к RabbitMQ
RABBIT_URL: str = 'amqp://guest:guest@10.111.122.51:5672'
RABBIT_INPUT_QUEUE: str = 'notify'

