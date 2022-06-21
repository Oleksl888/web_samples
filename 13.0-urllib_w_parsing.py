"""In this assignment you will write a Python program somewhat similar to https://py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and
extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter valid URL: ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
mylist = tree.findall('comments/comment')
sum = 0
for num in mylist:
    sum += int(num.find('count').text)
    print(num.find('name').text)
print(sum)
