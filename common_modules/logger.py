import uvicorn.middleware.message_logger as ml
import logging
import sys


def get_logger(module_name: str) -> logging.Logger:
    """
    Функция возвращает настроенный логер
    :param module_name: Имя модуля
    :return: logging.Logger
    """

    logger = logging.getLogger(module_name)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setFormatter(formatter)
    logger.addHandler(std_handler)
    # file_handler = logging.FileHandler(filename='debug.log')
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
    # logger.setLevel(settings.LOGGER_LEVEL)
    # logger.setLevel()
    return logger


def custom_uvicorn_middleware_logger(message):
    """Расширение стандартного логирования Uvicorn
    Заменяет <{length} bytes> на полноценное сообщение
    """
    return message
# Переопределение стандартной функции Uvicorn на свою
ml.message_with_placeholders = custom_uvicorn_middleware_logger
