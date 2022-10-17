import sqlite3
import socket
from registration import registration

print("please enter your username")
usr = 'hipopasran'
print("please enter your password")
psd = 'kronbars2017'

# with sqlite3.connect('../db/database.db') as db:
#     cursor = db.cursor()
#     cursor.execute("SELECT username, password FROM users WHERE username = :name", {"name": usr})
#     out = cursor.fetchone()
#     db.commit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2006))

data = client.recv(1024)
print(data.decode('utf-8'))
# toServ = (str(usr) + str(psd)).encode('utf-8')
# server.send(toServ)
client.send(usr.encode())
msg = client.recv(1024)
client.send(psd.encode())
get_usr = client.recv(1024).decode()
msg2 = client.send('usr got'.encode('utf-8'))
get_psd = client.recv(1024).decode()
print(get_usr)

if get_usr != None:
    db = {get_usr: get_psd}
else:
    db = {}

def authorization(usrnm, psswrd):
    if usrnm in db:
        if db[usrnm] == psswrd:
            status = 'Authorization successful'
        else:
            status = "Wrong password.Try again!"
    else:
        status = 'There is no such user. Please register Y/N?'
    return status

if __name__ == '__main__':
    print(authorization(usr, psd))

if authorization(usr, psd) == 'There is no such user. Please register Y/N?':
    agreement = input()
    if agreement.lower() == 'y':
        registration()
    elif agreement.lower() == 'n':
        print('Registration denied')
    else:
        print('Error')









