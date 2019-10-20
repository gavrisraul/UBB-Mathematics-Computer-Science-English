from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while(1):
    sentence = input('input sentence: ')
    if(sentence == "close"):
        break
    clientSocket.send(sentence.encode())
    retSentence = clientSocket.recv(1024)
    print('From server; ', retSentence.decode())

clientSocket.close()
