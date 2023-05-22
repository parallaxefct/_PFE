#enter a location / parse the returned JSON data and retrieve the PLACE_ID
import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?' #provide the intial url


address = input('Enter Location: ') #prompt for location
ad_key = {'address' : address, 'key' : 42} #create a dictionary and create key:value for address and key.

url = serviceurl + urllib.parse.urlencode(ad_key) #encode location and concantenate to serviceurl
handle = urllib.request.urlopen(url) #create handle
data = handle.read().decode() #decode utf-8


peeled = json.loads(data) #convert data to dictionary

print(peeled['results'][0]['place_id'])
