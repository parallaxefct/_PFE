#retrieving data from a webserver


#--------------------REQUEST/RESPONSE-CYCLE--------------------#



#the following if how all of these actions are processed, known as the REQUEST/RESPONSE CYCLE:

#1. your're on a webpage and click a hyper-link
#2. your browser intercepts that action, searches through the current page and its HTML code. It finds the information needed (what WEBSERVER to connect to, what PORT to connect to, and what document to retrieve)
#3. the BROWSER then connects to the port (80) and sends a GET request to the PORT
#4. the WEBSERVER then parces that GET request and finds the document or data you're seeking
#5. the WEBSERVER then sends a RESPONSE back in the form an HTML
#6. the BROWSER reads that HTML data/code and produces the next page or whatever the link leads to






#***TELNET is a piece of software that allows you to connect to any server and any port and send data to it. however, it is done in an unsecurte manner***#

import socket
#priming the device for a connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#passes the HOST and the PORT used
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
