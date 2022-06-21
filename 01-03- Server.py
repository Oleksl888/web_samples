'''Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой.
Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму.
После успешного вычисления возвращать ответ клиенту.'''


import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        data = [int(x) for x in data.decode().split(',')]
        result = str(sum(data))
        socket.sendto(result.encode(), self.client_address)


if __name__=='__main__':
    with socketserver.UDPServer(('127.0.0.1', 8888), UDPHandler) as server:
        server.serve_forever()