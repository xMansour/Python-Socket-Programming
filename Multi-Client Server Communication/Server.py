from socket import *
from threading import *

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message)

    clientSocket.close()


hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "127.0.0.1"
portNumber = 7500
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print ("Waiting for connection...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()