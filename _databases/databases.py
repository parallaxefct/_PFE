import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import re


#build SQL database first

conn = sqlite3.connect('emaildb.sqlite') #creates database with name entered
cur = conn.cursor() #
cur.execute('DROP TABLE IF EXISTS Counts') #this does not create a table if a table named 'Counts' exists
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') #creates the table and establishes the attributes of the table


url = 'http://www.py4e.com/code3/mbox.txt?PHPSESSID=db28ef47ba30c9406b8c224cfb52fcce' # provide url
ua_change = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) # changes headers/user-agent
uhandle = urllib.request.urlopen(ua_change).read() # creates a handle
total_string = BeautifulSoup(uhandle, 'html.parser').decode() # parses HTML | returns an BS object | converts BS object to STRING


users_count = {} # blank dictionary | USE THIS


line_parse = total_string.split('\n')


for line in line_parse: # loops through each line
    if line.startswith('From: '): # line contains a single string starting with 'From: <email>'
        email = line.lstrip('From: ')#use lstrip() to remove unneeded string
        if email not in users_count:
            users_count[email] = 1
        else:
            users_count[email] += 1


print(users_count)

for line in users_count:
    #cycle through dictionary, take KEY and place into 'email' section of table, take VALUE and place into 'count' section of table


#figure out a way to capture the email, search through line_parse for occurances and add the name of email and occurances to dictionary as key|value
