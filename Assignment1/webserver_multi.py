from socket import *
import threading

serverPort = 8080

def handle_client(connectionSocket):
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

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("Concurrent web server running on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    t = threading.Thread(target=handle_client, args=(connectionSocket,))
    t.start()
