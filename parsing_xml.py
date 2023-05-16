import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

url = input('Enter the URL: ')
opened_url = urllib.request.urlopen(url).read()
#url_string = str(open_url)


node_tree = ET.fromstring(opened_url) #returns a tree based on parent and child nodes
lst = node_tree.findall('comments/comment') #follows path starting at parent node (comments) and ending at child node (comment).


for x in lst:
    num = int(x.find('count').text) #searches for count element within the comment node and pulls the text. then type casts to an int
    sum = sum + num

print(sum)
