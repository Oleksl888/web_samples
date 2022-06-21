'''Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети.
Он принимает сообщения определенного формата, в котором будет идентификатор устройства и
печатает новые подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный
идентификатор устройства на сервер, уведомляя о своем присутствии.'''


import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, address = self.request
        print(data.decode())
        address.sendto(b"Device Id received", self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(('127.0.0.1', 8888), UDPHandler) as server:
        server.serve_forever()