from common_modules.logger import get_logger
from common_modules.singleton import Singleton
import asyncio
import aio_pika
import uuid
import threading


class Rabbit(metaclass=Singleton):
    """
    Класс подключения к RabbitMQ
    """

    def __init__(self, url, connection_name):
        """
        Для инициализации класса нужен url подключения
        :param url: 'amqp://guest:guest@10.111.122.51:5672'
        """
        self.logger = get_logger('RABBITMQ')
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
            self.logger.error(ex)
            raise
        return self

    def declare_queue(self, queue_name: str):
        self.loop.run_until_complete(self._declare_queue(queue_name))

    async def _declare_queue(self, queue_name: str):
        self.logger.info(f'Объявление очереди {queue_name}')
        self.queue = await self.channel.declare_queue(
            queue_name, durable=True)

    async def send_message_async(self, queue: str, body: str, operation_id: uuid = None, expiration=None):
        """
        Асинхронная отправка сообщений
        :param queue: Очередь
        :param body: Сообщение
        :param operation_id: Идентификатор тразакции
        :param expiration: Время жизни сообщения
        :return: None
        """
        if not uuid:
            operation_id = uuid.uuid4()
        # raise RabbitSendException(f'{operation_id} Не уалось отправить сообщение в очередь')
        message = aio_pika.Message(body=str(body).encode(),
                                   correlation_id=operation_id,
                                   app_id=self.connection_name,
                                   expiration=expiration)
        try:
            await self.channel.default_exchange.publish(message, routing_key=queue)
            self.logger.info(f'{operation_id} Message sent success')
        except Exception as ex:
            self.logger.error(f'{operation_id} Error sending message\n\t{ex}')
            raise RabbitSendException('Ошибка отправки сообщения')

    def send_message(self, queue, body, operation_id: uuid = None):
        raise RabbitSendException('qwe')
        self.loop.create_task(self.send_message_async(queue, body, operation_id))

    def add_lister_handler(self, queue: str, handler, **kwargs):
        self.declare_queue(queue)
        self.loop.run_until_complete(self._add_lister_handler(queue, handler, **kwargs))

    async def _add_lister_handler(self, queue, handler, **kwargs):
        await self.queue.consume(handler)

    def run_listen(self):
        self.loop.run_forever()


class RabbitSendException(Exception):
    def __init__(self, message):
        super().__init__(message)
