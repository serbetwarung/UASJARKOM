from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # 1 detik timeout

serverName = '127.0.0.1'
serverPort = 12000

for i in range(1, 11):
    # waktu saat mengirim
    send_time = time.time()
    message = f"Ping {i} {send_time}"

    try:
        # kirim
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # mulai timer RTT
        start = time.time()

        # tunggu balasan
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        # stop timer RTT
        end = time.time()
        rtt = end - start

        print(f"Reply: {modifiedMessage.decode()} | RTT = {rtt:.6f} s")

    except timeout:
        print("Request timed out")

clientSocket.close()
