import socket

def findAns():
    pass

def reqAns(reqMsg):
    HOST = 'selenium'
    PORT = 7777
    clientMessage = reqMsg

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())

    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)

    client.close()