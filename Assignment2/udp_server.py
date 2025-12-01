from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

print("UDP Ping Server running...")

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.decode().upper()

    if rand < 4:  # simulate packet loss 40%
        continue

    serverSocket.sendto(message.encode(), address)
