from typing import Union

from common_modules.logger import get_logger
from common_modules.singleton import Singleton
import asyncio
import aio_pika
import uuid
import threading

logger = get_logger('RABBITMQ')


class Rabbit(metaclass=Singleton):
    """
    Класс подключения к RabbitMQ
    """
    def __init__(self, url, connection_name):
        """
        Для инициализации класса нужен url подключения
        :param url: 'amqp://guest:guest@10.111.122.51:5672'
        """
        self.url = url
        self.connection_name = connection_name
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self._init())


    def loop_forever(self):
        t = threading.Thread(target=self.loop.run_forever)
        t.start()

    async def _init(self):
        """
        Подключение к MQ
        :return:
        """
        try:
            self.connection = await aio_pika.connect_robust(self.url,
                                                            client_properties={'connection_name': self.connection_name},
                                                            loop=self.loop)
            self.channel = await self.connection.channel(publisher_confirms=False)
            await self.channel.set_qos(prefetch_count=5000)
            self.channel.transaction()
        except Exception as ex:
            logger.error(ex)
            raise
        return self

    def declare_queue(self, queue_name: str):
        self.loop.run_until_complete(self._declare_queue(queue_name))

    async def _declare_queue(self, queue_name: str):
        self.queue = await self.channel.declare_queue(
            queue_name, durable=True)

    async def send_message_async(self, queue: str, body: str, operation_id: uuid = None):
        """
        Асинхронная отправка сообщений
        :param queue: Очередь
        :param body: Сообщение
        :param operation_id: Идентификатор тразакции
        :return: None
        """
        if not uuid:
            operation_id = uuid.uuid4()
        logger.debug(f'{operation_id} Sending message to RabbitMQ')
        message = aio_pika.Message(body=str(body).encode(), correlation_id=str(operation_id))
        try:
            await self.channel.default_exchange.publish(message, routing_key=queue)
            logger.debug(f'{operation_id} Message sent success')
        except Exception as ex:
            logger.error(f'{operation_id} Error sending message\n\t{ex}')
            raise

    def send_message(self, queue, body, operation_id: uuid = None):
        self.loop.create_task(self.send_message_async(queue, body, operation_id))

    def run_listen(self):
        self.loop.run_forever()

    def add_lister_handler(self, queue: str, handler, **kwargs):
        self.declare_queue(queue)
        self.loop.run_until_complete(self._add_lister_handler(queue, handler, **kwargs))

    async def _add_lister_handler(self, queue, handler, **kwargs):
        # await self.rpc.register(queue, handler, **kwargs)
        # await self.master.create_worker(queue, handler, **kwargs)
        await self.queue.consume(handler)
