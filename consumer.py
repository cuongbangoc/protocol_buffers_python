import users_pb2
import sys
import config as cfg

import rabbit

r = rabbit.Rabbit()
list_users = users_pb2.ListUsers()

def show(list_users):
    for user in list_users.user:
        print("User ID: {}".format(user.id))
        print("User Name: {}".format(user.name))
        if user.HasField('email'):
            print("Email: {}".format(user.email))


def callback_rabbit(ch, method, properties, body):
    #print("Method: {}".format(method))
    #print("Properties: {}".format(properties))

    print("\n================================================\n")
    list_users.ParseFromString(body)
    show(list_users)
    print("\n================================================\n")

try:
    # Receive Data from rabbit
    r.receive(cfg.QUEUE_TOPIC, callback_rabbit)
except Exception as e:
    print("receive data is error")
    print(e)
