'''Создайте HTTP клиента, который будет принимать URL ресурса, тип метода и словарь в
качестве передаваемых данных (опциональный). Выполнять запрос с полученным методом на полученный
ресурс, передавая данные соответствующим методом, и печатать на консоль статус код, заголовки и тело ответа.'''


import urllib.request
import json


optional_dict = {'dict': 5}
jsonized = json.dumps(optional_dict)
url = 'http://example.com'
with urllib.request.urlopen(url) as request:
    print(request.headers)
    print(request.msg)
    print(request.status)
    print(request.read().decode())
