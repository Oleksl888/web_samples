import urllib.request, urllib.parse, urllib.error
import json


url = input('Enter valid URL: ')
data = """{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}"""

info = json.loads(data)
print(info)
for i in range(len(info['comments'])):
    sum += int(info['comments'][i]['count'])
print(sum)
