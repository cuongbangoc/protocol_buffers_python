import users_pb2
import sys
import config as cfg
import rabbit

r = rabbit.Rabbit()
list_users = users_pb2.ListUsers()

def input(user):
    user.id = int(raw_input("Enter User ID: "))
    user.name = raw_input("Enter name: ")
    email = raw_input("Enter email address (blank for none): ")

    if email != '':
        user.email = email

def send_rabbit(data):
    # Connect to RabbitMQ and create channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
    channel = connection.channel()
    # Declare queue to send data
    channel.queue_declare(queue=cfg.QUEUE_TOPIC)
    # Send data
    channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=data)
    print(" [x] Sent data to RabbitMQ")
    connection.close()


try:
    # Add list users
    input(list_users.user.add())
    # encode data
    data_encode = list_users.SerializeToString()
    # Send to rabbit
    r.send(cfg.QUEUE_TOPIC, data_encode)

except Exception as e:
    print("Send data is error")
    print(e)
