from BSSAPI import settings
import logging
import sys


def get_logger(mod_name):
    logger = logging.getLogger(mod_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(filename='debug.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(std_handler)
    logger.addHandler(file_handler)
    logger.setLevel(settings.LOGGER_LEVEL)
    return logger
