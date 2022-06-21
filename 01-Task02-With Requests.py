'''Создайте HTTP клиента, который будет принимать URL ресурса, тип метода и словарь в
качестве передаваемых данных (опциональный). Выполнять запрос с полученным методом на полученный
ресурс, передавая данные соответствующим методом, и печатать на консоль статус код, заголовки и тело ответа.'''


import requests
import json


optional_dict = {'dict': 5}
jsonized = json.dumps(optional_dict)
url = 'http://example.com'
result = requests.get(url)
#print(result.text)
print(result.status_code)
print(result.headers)
print(result.request)
result = requests.post(url, data=optional_dict)
print(result.status_code)
print(result.headers)
print(result.text)
print(result.request)