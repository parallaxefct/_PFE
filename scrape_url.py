#read HTML from data files, parse the data, extract the numbers and find the sum total of all numbers listed on website
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


#this is to ignore any SSL certificate errors if the certificate is not part of pythons list
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#provide url, assign entire string to varible, parse string via BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

site = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html') #requesting site and opening in SITE variable
html = urlopen(site, context=ctx).read()
sifter = BeautifulSoup(html, 'html.parser')
