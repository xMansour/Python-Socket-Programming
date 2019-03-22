from socket import *
from threading import *

def sendMessage(clientSocket):
    while True:
        clientMessage = input()
        clientSocket.send(clientMessage.encode("utf-8"))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))

inputThread = Thread(target=sendMessage, args=(clientSocket, ))
inputThread.daemon = True
inputThread.start()

while True:
    serverMessage = clientSocket.recv(1024).decode("utf-8")
    print(serverMessage)


clientSocket.close()