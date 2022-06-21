'''Используя сервис https://jsonplaceholder.typicode.com/ попробуйте построить различные
типы запросов и обработать ответы. Необходимо попрактиковаться с urllib и библиотекой requests.
Рекомендуется сначала попробовать выполнить запросы, используя urllib, а затем попробовать реализовать
то же самое используя requests'''
#You can use GET, POST, PUT, PATCH and DELETE. Changes aren't persisted between calls.


import urllib.request
import requests
import json


url_db = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/db'
url_posts = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/posts'
url_posts1 = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/posts/1'
url_profile = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/profile'
data = {"title" : "Make a POST call", "body": "Details of making post call ....", "userId": 1}
data2 = {"title": "Alex", "userId": 101}
data3 = {"title": "Alex", 'bla': '333'}
jsonized = json.dumps(data)
jsonized2 = json.dumps(data2)
jsonized3 = json.dumps(data3)
headers = {"Content-Type": "application/json"}

result = requests.get(url_db)
#print(result.text)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
returned = result.json()
print(returned)

result = requests.post(url_posts, data=jsonized, headers=headers)
#print(result.text)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
returned = result.json()
print(returned)

result = requests.put(url_posts1, data=jsonized3, headers=headers)
#print(result.text)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
returned = result.json()
print(returned)

result = requests.patch(url_posts1, data=jsonized3, headers=headers)
#print(result.text)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
returned = result.json()
print(returned)

result = requests.delete(url_posts1, headers=headers)
#print(result.text)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
returned = result.json()
print(returned)

