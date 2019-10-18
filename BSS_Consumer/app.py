import asyncio
import aio_pika
from BSS_Consumer.settings import *


async def process_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print(message.body)
        await asyncio.sleep(1)


async def main(loop):
    connection = await aio_pika.connect_robust(
        RABBIT_URL, loop=loop
    )

    queue_name = RABBIT_QUEUE_NOTIFY

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be
    # processing at the same time.
    await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(
        queue_name, auto_delete=True
    )

    await queue.consume(process_message)

    return connection


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main(loop))

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())