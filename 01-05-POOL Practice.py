'''Изучите более подробно и попробуйте возможности настройки, pull-а соединений
и его режимов. Используя утилиту ab протестируйте ваши наработки (https://ru.wikipedia.org/wiki/ApacheBench)'''


import urllib3
import requests
import json


url = 'https://httpbin.org/get'
p_url = 'https://httpbin.org/post'
a_url = 'http://google.com/'
manager = urllib3.PoolManager(num_pools=2)
request = manager.request('GET', url)
request2 = manager.request('POST', p_url, body=json.dumps({'Alex':5}), headers={'Content-Type': 'application/json'})
request3 = manager.request('GET', a_url)
print(request.data.decode())
print(request2.data.decode())
print(request3.data.decode())
