from socket import *

try:
    hostSocket = socket(AF_INET, SOCK_STREAM)
    hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    hostIp = "127.0.0.1"
    portNumber = 7500
    hostSocket.bind((hostIp, portNumber))
    hostSocket.listen(1)
    print ("Waiting for connection...")
    clientSocket, clientIp = hostSocket.accept()
    print ("Connection established with: ", clientIp[0])
    while True:
        clientMessage = clientSocket.recv(2048)
        print ("Client says: ", clientMessage.decode("utf-8"))
        serverMessage = input("Server says: ")
        clientSocket.send(serverMessage.encode("utf-8"))
    hostSocket.close()


except error:
    print(error)

except KeyboardInterrupt:
    print(KeyboardInterrupt)