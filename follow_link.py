#
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

names = []

#provide url, assign entire string to varible, parse string via BeautifulSoup
def parse_url(url):
    html = urllib.request.urlopen(url).read()
    sifter = BeautifulSoup(html, 'html.parser')
    #sifter pulls html anchors and assigns to 'tags' varibale
    tags = sifter('a', None)
    return tags

def cycle_links(tags_parsed, position):
    for tag in tags_parsed:
        #gets HTML tag as string
        x = tag.get('href', None)
        position -= 1

        if position == 0:
            break
    return x

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


tags_parsed = parse_url(url)
all_links = cycle_links(tags_parsed, position)

print(all_links)

#iterates through tags_parsed

#    name = re.findall('(E.+)[.]', x)
