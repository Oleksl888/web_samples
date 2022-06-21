'''Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой.
Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму.
После успешного вычисления возвращать ответ клиенту.'''


import socket

nums = b'1, 2'
mysock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysock.connect(('127.0.0.1', 8888))
mysock.sendall(nums)
print(mysock.recv(64).decode())
mysock.close()