import users_pb2
import sys
import pika
import config as cfg

def show(list_users):
    for user in list_users.user:
        print("User ID: {}".format(user.id))
        print("User Name: {}".format(user.name))
        if user.HasField('email'):
            print("Email: {}".format(user.email))

def receive_rabbit(list_users):
    # Connect to RabbitMQ and create channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
    channel = connection.channel()

    # Declare and listen queue
    channel.queue_declare(queue=cfg.QUEUE_TOPIC)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    # Function process and print data
    def callback(ch, method, properties, body):
        #print("Method: {}".format(method))
        #print("Properties: {}".format(properties))
        list_users.ParseFromString(body)
        show(list_users)
    # Listen and receive data from queue
    channel.basic_consume(callback, queue=cfg.QUEUE_TOPIC,no_ack=True)
    channel.start_consuming()

file_name = 'data'
list_users = users_pb2.ListUsers()

# Read existing list users
try:
    f = open(file_name, 'rb')
    #list_users.ParseFromString(f.read())
    f.close()

    #show(list_users)

    # Receive Data from rabbit
    receive_rabbit(list_users)
except Exception as e:
    print("Read data is error")
