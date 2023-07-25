#this scraper is built to work with urls/embedded links. hence the use of anchor tags
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

#iterate through each line of tags, GET string that begins with href, extract the name if it starts with an E, and IF the name variable returns a list with the length greater than 0 append to names list
for tag in tags:
    x = tag.get('href', None)
    print(x)
    name = re.findall('(E.+)[.]', x) #logic: () indicates starts and stop // E is the character that is searched for to start the 'scan' // the '.' matches to ANY character after the E // the '+' will repeat to characters after // () looks to end the 'scan' and '[.] is the character that is searched for to end the scan'
    if len(name) > 0:
        names.append(name[0])
print(names)
