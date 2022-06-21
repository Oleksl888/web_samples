"""Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL."""

import socket
import re

while True:
    try:
        website = input("Enter URL: ")
        domain = re.findall('^http[s]?://[w]*[.]?(\S+?)/', website)
        if len(domain) == 1:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysocket.connect((domain[0], 80))
            break
    except:
        print('Must Enter Valid URL')
cmd ='GET ' + website + ' HTTP/1.0\r\n\r\n'
print(cmd)
mysocket.send(cmd.encode())
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    if '400 Bad' in data.decode() or '404 Not Found' in data.decode():
        print('Bad URL')
        break
    print(data.decode(), end='')
mysocket.close()
