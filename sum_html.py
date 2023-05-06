#read HTML from data files, parse the data, extract the numbers and find the sum total of all numbers listed on website
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


#this is to ignore any SSL certificate errors if the certificate is not part of pythons list
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#provide url, assign entire string to varible, parse string via BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_1492883.html'
html = urlopen(url, context=ctx).read()
sifter = BeautifulSoup(html, 'html.parser')

#establish sum varible as INT to use later in while loop to find sum
sum = 0
tags = sifter('span', None)

#
for tag in tags:
    decoded_tag = tag.decode().strip()
    x = re.findall('[0-9]+', decoded_tag)
    #counter
    print(type(x))
    counter = len(x)
    #capture each string, convert to interger and find the sum
    while counter != 0:
        num = int(x[(counter - 1)])
        sum = sum + num
        counter -= 1

print(sum)
