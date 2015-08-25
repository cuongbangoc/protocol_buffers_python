import users_pb2
import sys
import pika
import config as cfg

def input(user):
    user.id = 1
    user.name = "cuongbn"
    email = "cuongbn@sigma-solutions.eu"

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


file_name = 'data'
list_users = users_pb2.ListUsers()

# Read the existing user
try:
    f = open(file_name, 'rb')
    list_users.ParseFromString(f.read())
    f.close()
except IOError as e:
    print("file {} not exist. Creating a new file".format(file_name))

# Add list users
input(list_users.user.add())

# Write the new list users to file
try:
    #f = open(file_name, 'wb')
    data_encode = list_users.SerializeToString()
    # Send to rabbit
    send_rabbit(data_encode)

    #f.write(data_encode)
    #f.close()
except Exception as e:
    print("Write file is error")
    print(e)
