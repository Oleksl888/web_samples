'''Создайте сокет-сервер, который будет ожидать подключения по tcp-протоколу и запускать
сокет-клиентов, которые подключаются на TCP сокет. Используйте примеры для создания TCP
сокетов из предыдущих примеров. В качестве примера сервера можно использовать вычисление
произведения двух чисел, где клиент отправляет два числа на tcp-сокет, а сервер отвечает
результатом сложения и ожидает от клиента новую пару чисел. В случае если сокет послал
сообщение с текстом close, то закрывать соединение с обеих сторон и завершать выполнение потока обработки клиента.'''

import socket
import socketserver
import threading
import asyncio

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(('localhost', 8888))


def server_app(client=None):
    while True:
        print('Ready to receive data...')
        received = client.recv(64).decode()
        print('Data Received')
        if received == 'close':
            print('Closing client...')
            client.close()
            print('Client closed...')
            break
        nums = str(sum([float(num) for num in received.split()]))
        print('Sending data to client...')
        client.sendall(nums.encode())
        print('Data sent to client!')


if __name__ == '__main__':
    while True:
        mysock.listen(2)
        print('Waiting for connection...')
        client, address = mysock.accept()
        print('Connection established')
        params = {'client': client}
        thread = threading.Thread(target=server_app, kwargs=params)
        thread.start()
        # thread.join()
        print(threading.active_count())
        print(threading.enumerate())


# class ClientThread(threading.Thread):
#      def __init__(self, clientAddress, clientsocket):
#           threading.Thread.__init__(self)
#           self.csocket = clientsocket
#           print ("New connection added: ", clientAddress)
#
#      def run(self):
#           print ("Connection from : ", clientAddress)
#           #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
#           msg = ''
#           while True:
#                data = self.csocket.recv(2048)
#                msg = data.decode()
#                if msg=='bye':
#                     break
#                print ("from client", msg)
#                self.csocket.send(bytes(msg,'UTF-8'))
#                print ("Client at ", clientAddress , " disconnected...")
#
#
# LOCALHOST = "localhost"
# PORT = 8888
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((LOCALHOST, PORT))
# print("Server started")
# print("Waiting for client request..")
# while True:
#      server.listen(1)
#      clientsock, clientAddress = server.accept()
#      newthread = ClientThread(clientAddress, clientsock)
#      newthread.start()
