from BSSAPI.logger import get_logger
import asyncio
import aio_pika
import uuid

logger = get_logger('RABBITMQ')


class Rabbit:
    """
    Класс подключения к RabbitMQ
    """
    def __init__(self, url):
        """
        Для инициализации класса нужен url подключения
        :param url: 'amqp://guest:guest@10.111.122.51:5672'
        """
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self._init())

    async def _init(self):
        """
        Подключение к MQ
        :return:
        """
        try:
            self.connection = await aio_pika.connect_robust(self.url, loop=self.loop)
            self.channel = await self.connection.channel(publisher_confirms=False)
            self.channel.transaction()
        except Exception as ex:
            logger.error(ex)
        return self

    async def send_message_async(self, queue: str, body: str, operation_id: uuid = None) -> bool:
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
        message = aio_pika.Message(body=body.encode())
        try:
            await self.channel.default_exchange.publish(message, routing_key=queue)
            logger.debug(f'{operation_id} Message sent success')
        except Exception as ex:
            logger.error(f'{operation_id} Error sending message')
            raise

    def send_message(self, queue, body):
        asyncio.ensure_future(self.send_message_async(queue, body), loop=self.loop)
