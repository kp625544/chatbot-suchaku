#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get server ip
port = 4447                # Reserve a port for your service.

s.connect((host, port))

#here the magic starts

while True:
   print s.recv(1024)
   #s.send(raw_input("> "))
   while 1:
    s.send(raw_input("> ").encode())
    print s.recv(1024)


s.close()                     # Close the socket when done
