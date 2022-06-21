'''Разработайте сокет сервер на основе библиотеки asyncio. Сокет сервер должен выполнять
сложение двух чисел, как из предыдущего примера по многопоточности.'''

import socket
import asyncio


async def request_handler(client=None):
    while True:
        print('Ready to receive data...')
        received = await loop.sock_recv(client, 64)
        received = received.decode()
        print('Data Received')
        if received == 'close':
            print('Closing client...')
            client.close()
            print('Client closed...')
            break
        nums = str(sum([float(num) for num in received.split()]))
        print('Sending data to client...')
        await loop.sock_sendall(client, nums.encode())
        print('Data sent to client!')


async def server_app():
    while True:
        mysock.listen(2)
        print('Waiting for connection...')
        client, address = await loop.sock_accept(mysock)
        print(f'Connection established with {address}')
        # params = {'client': client}
        # thread = threading.Thread(target=request_handler, kwargs=params)
        # thread.start()
        loop.create_task(request_handler(client))
        # print(f'Currently running {threading.active_count()} threads')


if __name__ == '__main__':
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.bind(('localhost', 8888))
    loop = asyncio.get_event_loop()
    loop.create_task(server_app())
    loop.run_forever()
