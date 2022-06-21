import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter Location: ')
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
search = {'address' : address, 'api_key' : api_key}
url = serviceurl + urllib.parse.urlencode(search)
print(url)
data = urllib.request.urlopen(url).read()
location = json.loads(data.decode())
print(json.dumps(location, indent=4))
print(location['results'][0]['place_id'])
