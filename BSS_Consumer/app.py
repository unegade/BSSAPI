from BSS_Consumer.settings import *
from BSS_Consumer.workers.default_process import process_message
from common_modules.rabbit import Rabbit
import logging


if __name__ == "__main__":
    logging.basicConfig(level=LOGGER_LEVEL)
    rb = Rabbit(RABBIT_URL, 'Consumer')
    rb.add_lister_handler(RABBIT_INPUT_QUEUE, process_message)
    # for i in [i for i in range(10000)]:
    #     rb.send_message('notify', i, i)
    rb.run_listen()
