import pika
from BSSAPI.logger import logger


class Rabbit:
    def __init__(self, host: str = 'localhost', port: int = 5672, user: str = 'guest', password: str = 'guest'):
        self.credential = pika.PlainCredentials(user, password)
        self.parameters = pika.ConnectionParameters(host=host, port=port,
                                                    credentials=self.credential,
                                                    connection_attempts=1, retry_delay=1)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.channel

    def __repr__(self) -> str:
        return f'{self.parameters.host}:{self.parameters.port} - {self.credential.username}'

    def connect(self, queue):
        try:
            self.channel = self.connection.channel()
            if queue:
                self.channel.queue_declare(queue=queue, durable=True)
        except Exception as ex:
            print('qe')
            logger.error(f'Connect to {"self"} failed. Error message:\n{ex}')
            print('qe')
        return self.channel

    def send_message(self, queue: str, body: str, exchange: str = ''):
        self.channel.basic_publish(exchange=exchange, routing_key=queue, body=body,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2
                                   ))

    def close(self):
        self.connection.close()

# rb = Rabbit('10.111.122.51')
# rb.connect('notify')
# for i in range(500):
#     rb.send_message('notify','qweqweqw')
