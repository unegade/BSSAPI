import pika
from BSSAPI.logger import get_logger
import asyncio
import aio_pika
import logging

logger = get_logger(__name__)

class Rabbit:
    def __init__(self, url):
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self._init())

    async def _init(self):
        try:
            self.connection = await aio_pika.connect_robust(self.url, loop=self.loop)
            self.channel = await self.connection.channel(publisher_confirms=False)
            self.channel.transaction()
        except Exception as ex:
            logger.error(ex)
        return self

    def connect(self):
        try:
            self.loop.run_until_complete(self._init())
        except Exception as ex:
            logger.error(ex)


    async def _send_message(self, queue, body: str):
        message = aio_pika.Message(body=body.encode())
        await self.channel.default_exchange.publish(message, routing_key=queue)

    def send_message(self, queue, body):
        self.loop.run_until_complete(self._send_message(queue, body))
