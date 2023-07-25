import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import re


#build SQL database first

#conn = sqlite3.connect('emaildb.sqlite') #creates database with name entered
#cur = conn.cursor() #
#cur.execute('DROP TABLE IF EXISTS Counts') #this does not create a table if a table named 'Counts' exists
#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''') #creates the table and establishes the attributes of the table


url = 'http://www.py4e.com/code3/mbox.txt?PHPSESSID=db28ef47ba30c9406b8c224cfb52fcce' # provide url
ua_change = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) # changes headers/user-agent
uhandle = urllib.request.urlopen(ua_change).read() # creates a handle
total_string = BeautifulSoup(uhandle, 'html.parser').decode() # parses HTML | returns an BS object | converts BS object to STRING


users_count = {} # blank dictionary | USE THIS


for line in total_string: # loops through each line
    if line.startswith('From: '): # if line starts with "From: "
        line_parse = line.split() # then split line by white spaces and return list as line_parse
        if line_parse[1] not in users_count:
            users_count[line_parse[1]] = 1
        else:
            users_count[line_parse[1]] += 1

print(users_count)


#figure out a way to capture the email, search through line_parse for occurances and add the name of email and occurances to dictionary as key|value 
