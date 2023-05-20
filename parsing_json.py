#takes URL, parses JSON, and returns sum of count

import urllib.request, urllib.parse, urllib.error
import json


url = 'http://py4e-data.dr-chuck.net/comments_1492886.json' #provided URL
handle = urllib.request.urlopen(url) #establish a handle
data = handle.read().decode() #read and place data into variable and decode from UTF-8

sum = 0

peeled = json.loads(data) #this parses JSON data

for line in peeled['comments']: #loops through each dictionary in comments list
    num = line['count'] #extracts count value
    sum = sum + num #computes sum
print(sum)
