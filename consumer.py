import users_pb2
import sys

def show(list_users):
    for user in list_users.user:
        print("User ID: {}".format(user.id))
        print("User Name: {}".format(user.name))
        if user.HasField('email'):
            print("Email: {}".format(user.email))

file_name = 'data'
list_users = users_pb2.ListUsers()

# Read existing list users
try:
    f = open(file_name, 'rb')
    list_users.ParseFromString(f.read())
    f.close()

    show(list_users)
except Exception as e:
    print("Read data is error")
