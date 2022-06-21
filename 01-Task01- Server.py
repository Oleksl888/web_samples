'''Создать простой чат, на основе TCP протокола, который позволит подключаться нескольким
клиентам и обмениваться сообщениями.'''


import socket
import json
from datetime import datetime


#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.bind(('127.0.0.1', 8888))
#mysock.listen(5)
#connections = []

#while True:
#    try:
#        print("Waiting for client")
#        client, address = mysock.accept()
#        print(client)
#        print(address)
#    except KeyboardInterrupt:
#        mysock.close()
#    else:
#        print('Data Received')
#        received = client.recv(512).decode()
#        received = json.loads(received)
#        received['timestamp'] = datetime.now()
#        connections.append(received)
#        print(connections)
#        for num, msg in enumerate(connections):
#            if received['username'] == msg['sendto']:
#                mess = f'@{msg["timestamp"]}: {msg["username"]} said: {msg["message"]}'
#                client.sendall(mess.encode())
#                del connections[num]
#        else:
#            client.sendall(b'You have 0 new messages')
#        print('Client data received')
#        client.close()


import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    _connections = []


    def handle(self):
        data = self.request.recv(512).decode()
        received = json.loads(data)
        received['timestamp'] = datetime.now()
        if len(received['sendto']) > 0:
            self._connections.append(received)
        print(self._connections)
        for num, msg in enumerate(self._connections):
            if received['username'] == msg['sendto']:
                mess = f'@{msg["timestamp"]}: {msg["username"]} said: {msg["message"]}'
                self.request.sendall(mess.encode())
                del self._connections[num]
        else:
            self.request.sendall(b'You have 0 new messages')


if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 8888), EchoTCPHandler) as server:
        server.serve_forever()