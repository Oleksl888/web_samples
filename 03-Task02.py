'''Создайте сопрограмму, которая получает контент с указанных ссылок и логирует ход выполнения
в специальный файл используя стандартную библиотеку urllib, а затем проделайте то же самое с
библиотекой aiohttp. Шаги, которые должны быть залогированы: начало запроса к адресу X,
ответ для адреса X получен со статусом 200. Проверьте ход выполнения программы на >3 ресурсах
и посмотрите последовательность записи логов в обоих вариантах и сравните результаты. Для двух
видов задач используйте разные файла для логирования, чтобы сравнить полученный результат.'''

import urllib.request
import asyncio
import aiohttp
import datetime


url_list = [
    'http://example.com/',
    'http://google.com/',
    'https://www.wikipedia.org/',
    'http://youtube.com/'
]


async def get_content(url):
    print(f'Starting request to {url}....')
    response = urllib.request.urlopen(url)
    await response.text()
    print(f'Request status received for url {response.url} code {response.status} at {datetime.datetime.now()}')


event_loop = asyncio.get_event_loop()
tasklist = [event_loop.create_task(get_content(url)) for url in url_list]
tasks = asyncio.wait(tasklist)
event_loop.run_until_complete(tasks)
event_loop.close()



