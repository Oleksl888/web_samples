"""Exercise 5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember
that recv receives characters (newlines and all), not lines."""

import socket
import re

website = input('Enter Valid Website URL: ')
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
domain = re.findall('h.+/[w]*[.]?(\S+)/', website)
mysocket.connect((domain[0], 80))
request = 'GET ' + website + ' HTTP/1.0\r\n\r\n'
mysocket.send(request.encode())
while True:
    data = mysocket.recv(1000)
    if len(data) < 1: break
    if '\r\n\r\n' in data.decode():
        num = data.decode().find('\r\n\r\n')
        print(data.decode()[num + 1:], end='')
        break
while True:
    data = mysocket.recv(1000)
    if len(data) < 1: break
    print(data.decode(), end='')
mysocket.close()