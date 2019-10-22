from aio_pika import IncomingMessage
from common_modules.logger import get_logger
import asyncio

logger = get_logger(__name__ )

async def process_message(message: IncomingMessage):
    async with message.process():
        logger.debug(f'{message.correlation_id}, {message.body.decode()}')
        await asyncio.sleep(1)
        logger.info(f'{message.correlation_id}, Process completed')
