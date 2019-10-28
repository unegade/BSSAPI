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
    return logger


def override_library_loggers(*lib_names):
    for name in lib_names:
        uvi_log = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
        std_handler = logging.StreamHandler(sys.stdout)
        std_handler.setFormatter(formatter)
        uvi_log.addHandler(std_handler)


def custom_uvicorn_middleware_logger(message):
    """Расширение стандартного логирования Uvicorn
    Заменяет <{length} bytes> на полноценное сообщение
    """
    return message


# Переопределение стандартной функции Uvicorn на свою
ml.message_with_placeholders = custom_uvicorn_middleware_logger
# Подлючение сторонних логеров к стандартому выводу
override_library_loggers('uvicorn')
