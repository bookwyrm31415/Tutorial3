# This is a very basic HTTP server which listens on port 8080,
# and serves the same response messages regardless of the browser's request. It runs on python v3
# Usage: execute this program, open your browser (preferably chrome) and type http://servername:8080
# e.g. if server.py and broswer are running on the same machine, then use http://localhost:8080

# Import the required libraries
from socket import *
import base64


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
    request = connectionSocket.recv(1024)
    print(request)
    if "index" in str(request):
        # create HTTP response
        response = "HTTP /1.1 200 OK\r\n\r\n"

        # send HTTP response back to the client
        connectionSocket.send(response.encode())

        # encode html file
        file = open('index.html', 'rb')
        data = file.read()

        connectionSocket.send(data)

    elif 'picture' in str(request):
        # create HTTP response
        response = "HTTP /1.1 200 OK Content-Type: image/png\r\n\r\n"

        # send HTTP response back to the client
        connectionSocket.send(response.encode())

        # encode html file
        with open("picture.png",'rb') as image:
            image = image.read()
            connectionSocket.send(image)


    elif 'image2' in str(request):
        # create HTTP response
        response = "HTTP /1.1 200 OK Content-Type: image/png\r\n\r\n"

        # send HTTP response back to the client
        connectionSocket.send(response.encode())

        # encode html file
        with open("image2.png",'rb') as image:
            image = image.read()
            connectionSocket.send(image)


    # Close the connection
    connectionSocket.close()
