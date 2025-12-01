from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("Web server running on port", serverPort)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()

        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())

        for i in outputdata:
            connectionSocket.send(i.encode())

        connectionSocket.close()

    except IOError:
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.close()
