'''Используя сервис https://jsonplaceholder.typicode.com/ попробуйте построить различные
типы запросов и обработать ответы. Необходимо попрактиковаться с urllib и библиотекой requests.
Рекомендуется сначала попробовать выполнить запросы, используя urllib, а затем попробовать реализовать
то же самое используя requests'''
#You can use GET, POST, PUT, PATCH and DELETE. Changes aren't persisted between calls.


import urllib.request
import requests
import json


url_db = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/db'
url_posts = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/posts/1'
url_profile = 'https://my-json-server.typicode.com/Oleksl888/MJS-Practice/profile'
data = {"title" : "Make a POST call", "body": "Details of making post call ....", "userId": 1}
data2 = {"title": "Alex", "userId": 101}
data3 = {"title": "Alex"}
jsonized = json.dumps(data)
jsonized2 = json.dumps(data2)
jsonized3 = json.dumps(data3)
req = urllib.request.Request(url_db, method='GET')
result = urllib.request.urlopen(req)
#print(result.text)
print(result.status)
print(result.getcode())
print(result.reason)
returned = json.loads(result.read().decode())
print(returned)

req = urllib.request.Request(url_posts, method='DELETE', headers={"Content-Type": "application/json"})
result = urllib.request.urlopen(req)
#print(result.text)
print(result.status)
print(result.getcode())
print(result.reason)
returned = json.loads(result.read().decode())
print(returned)

req = urllib.request.Request(url_posts, method='POST', data=jsonized.encode(), headers={"Content-Type": "application/json"})
result = urllib.request.urlopen(req)
#print(result.text)
print(result.status)
print(result.getcode())
print(result.reason)
returned = json.loads(result.read().decode())
print(returned)

req = urllib.request.Request(url_profile, method='PUT', data=jsonized2.encode(), headers={"Content-Type": "application/json"})
result = urllib.request.urlopen(req)
#print(result.text)
print(result.status)
print(result.getcode())
print(result.reason)
returned = json.loads(result.read().decode())
print(returned)

