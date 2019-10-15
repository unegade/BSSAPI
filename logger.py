import logging
import sys
import settings

logger = logging.getLogger()
logger.setLevel(settings.LOGGER_LEVEL)

uvicornlog = logging.getLogger("uvicorn")
uvicornlog.setLevel(logging.ERROR)

# handler stdout logger
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
