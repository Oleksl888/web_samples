'''Создайте сокет-сервер, который будет ожидать подключения по tcp-протоколу и запускать
сокет-клиентов, которые подключаются на TCP сокет. Используйте примеры для создания TCP
сокетов из предыдущих примеров. В качестве примера сервера можно использовать вычисление
произведения двух чисел, где клиент отправляет два числа на tcp-сокет, а сервер отвечает
результатом сложения и ожидает от клиента новую пару чисел. В случае если сокет послал
сообщение с текстом close, то закрывать соединение с обеих сторон и завершать выполнение потока обработки клиента.'''


import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost', 8888))
while True:
    nums = input('Enter numbers you want to send: ')
    if nums == 'close':
        mysock.send(nums.encode())
        mysock.close()
        break
    mysock.send(nums.encode())
    result = mysock.recv(64).decode()
    print(result)
    # mysock.send(b'2')
    # print(mysock.recv(64))
