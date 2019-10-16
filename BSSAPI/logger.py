import logging
import sys
from BSSAPI import settings

logger = logging.getLogger()
logger.setLevel(settings.LOGGER_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


uvicornlog = logging.getLogger("uvicorn")
uvicornlog.setLevel(logging.ERROR)

# handler stdout logger
std_handler = logging.StreamHandler(sys.stdout)
std_handler.setFormatter(formatter)
logger.addHandler(std_handler)

file_handler = logging.FileHandler(filename='debug.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)