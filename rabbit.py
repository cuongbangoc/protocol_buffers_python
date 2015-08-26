import pika
import config as cfg

class Rabbit():
    def __init__(self):
        self.conn = None
        self.channel = None

    def connect(self):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
        self.channel = self.conn.channel()

    def close(self):
        self.conn.close()

    def send(self, topic, data):
        # Open connection
        self.connect()
        # Declare queue to send data
        self.channel.queue_declare(topic)
        # Send data
        self.channel.basic_publish(exchange='', routing_key=topic, body=data)
        print(" [x] Sent data to RabbitMQ")

        # Close connection
        self.close()

    def receive(self, topic, callback):
        # Open connection
        self.connect()
        # Declare queue to send data
        self.channel.queue_declare(topic)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        # Listen and receive data from queue
        self.channel.basic_consume(callback, queue=topic, no_ack=True)
        self.channel.start_consuming()


