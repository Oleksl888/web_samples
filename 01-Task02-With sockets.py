'''Создайте HTTP клиента, который будет принимать URL ресурса, тип метода и словарь в
качестве передаваемых данных (опциональный). Выполнять запрос с полученным методом на полученный
ресурс, передавая данные соответствующим методом, и печатать на консоль статус код, заголовки и тело ответа.'''


import socket


url = 'example.com'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url, 80))
request = [
    'GET / HTTP/1.1',
    'Host: example.com',
    '\n'
]
request = '\n'.join(request)
print(request)
mysock.sendall(request.encode())
data = mysock.recv(10240).decode()
status_code = data[:data.index('\r\n')]
headers = data[data.index('\r\n'):data.index('\r\n\r\n')]
body = data[data.index('\r\n\r\n'):]
print(headers)
print(status_code)
print('--------------------')
print(body)
mysock.close()
