'''Создать простой чат, на основе TCP протокола, который позволит подключаться нескольким
клиентам и обмениваться сообщениями.'''


import socket
import json


while True:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('127.0.0.1', 8888))
    sendto = input('Enter who is the message for ( Alex, Alexa): ')
    msg = input('Enter message here:...')
    message = {'username': 'Boris', 'sendto': sendto, 'message': msg}
    if msg == 'endchat':
        mysock.close()
        break
    mysock.send(json.dumps(message).encode())
    response = mysock.recv(512)
    print(response.decode())
    mysock.close()

