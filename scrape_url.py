#
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re


#provide url, assign entire string to varible, parse string via BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url).read()
sifter = BeautifulSoup(html, 'html.parser')

#sifter pulls html anchors and assigns to 'tags' varibale
tags = sifter('a', None)
#create blank list to capture names
names = []

for tag in tags:
    x = tag.get('href', None)
    #figure out regex to pull just the name and store it in the blank list created
    name = re.findall('E+', x)
    print(name)
