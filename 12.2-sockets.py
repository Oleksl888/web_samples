"""Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire docu-
ment and count the total number of characters and display the count
of the number of characters at the end of the document."""

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
mysocket.send(cmd.encode())
counter = 0
while True:
    data = mysocket.recv(500)
    counter += len(data)
    if len(data) < 1:
        print()
        print('The total number of symbols received is {}'.format(counter))
        break
    if '400 Bad' in data.decode() or '404 Not Found' in data.decode():
        print('Bad URL')
        break
    if counter <= 3000:
        print(data.decode(), end='')
mysocket.close()
