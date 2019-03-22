from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))

while True:
    clientMessage = input("Message: ")
    clientSocket.send(clientMessage.encode("utf-8"))
clientSocket.close()