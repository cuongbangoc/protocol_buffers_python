import users_pb2
import sys

def input(user):
    user.id = 1#int(sys.raw_input("Enter user ID: "))
    user.name = "cuongbn"#raw_input("Enter name: ")
    email = "cuongbn@sigma-solutions.eu"#raw_input("Enter email address (blank for none): ")
    
    if email != '':
        user.email = email


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
    f = open(file_name, 'wb')
    data_encode = list_users.SerializeToString()
    f.write(data_encode)
    f.close()
except Exception as e:
    print("Write file is error")
