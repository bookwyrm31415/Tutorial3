# This is a very basic HTTP server which listens on port 8080,
# and serves the same response messages regardless of the browser's request. It runs on python v3
# Usage: execute this program, open your browser (preferably chrome) and type http://servername:8080
# e.g. if server.py and broswer are running on the same machine, then use http://localhost:8080

# Import the required libraries
import mimetypes
from os import path
from socket import *


# Listening port for the server


serverPort = 8080

# Create the server socket object
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server socket to the port
serverSocket.bind(('', serverPort))

# Start listening for new connections
serverSocket.listen(1)

print('The server is ready to receive messages')

while 1:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()

    # Retrieve the message sent by the client
    request = connectionSocket.recv(1024).decode()
    print(request)
    filename = request.split(' ')[1][1:]
    # create HTTP response
    if path.exists(filename):
        header = "HTTP/1.0 200 OK\r\n\r\n"

        mime = mimetypes.guess_type(filename)
        if 'text' in mime[0]:
            mode = 'r'
        else:
            mode = 'rb'

        with open(filename, mode) as file:
            body = file.read()
    else:
        header = "HTTP/1.0 404 Not Found\r\n\r\n"
        body = "404 Error Sorry"

    if not isinstance(body, bytes):
        body = body.encode()
    response = header.encode() + body

    if not isinstance(response, bytes):
        response = response.encode()
    connectionSocket.send(response)

    # Close the connection
    connectionSocket.close()
