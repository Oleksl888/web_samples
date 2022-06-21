'''Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети.
Он принимает сообщения определенного формата, в котором будет идентификатор устройства и
печатает новые подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный
идентификатор устройства на сервер, уведомляя о своем присутствии.'''


import socket
from time import sleep


while True:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mysock.connect(('127.0.0.1', 8888))
    mysock.sendall(b'ID of this device')
    print(mysock.recv(64).decode())
    mysock.close()
    sleep(2)