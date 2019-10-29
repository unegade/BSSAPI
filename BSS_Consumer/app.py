from BSS_Consumer.workers.default_process import process_message
from common_modules.config import Config
from common_modules.rabbit import Rabbit
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if Config.get('DEFAULT', 'log_level') == 'debug' else logging.INFO)
    rb = Rabbit(url=Config.get('RABBIT', 'url'),
                connection_name=Config.get('DEFAULt', 'app_name'))
    rb.add_lister_handler(Config.get('DEFAULT', 'input_queue'), process_message)
    rb.run_listen()
