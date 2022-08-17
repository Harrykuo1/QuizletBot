import socket
from linebot.models import TextSendMessage

def searchScore(reqMsg, uid):
    message = []
    HOST = 'ecourse'
    PORT = 8888
    reqMsg = reqMsg.replace(" ","")

    account = "xxxxxxxx"
    password = "xxxxxx"
    if(len(reqMsg) == 0):
        clientMessage = account + " " + password
    else:
        clientMessage = account + " " + password + " " + reqMsg


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())

    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)

    resMsgText = 'Receive: ' + serverMessage
    message.append(TextSendMessage(text=resMsgText))
    client.close()

    return message
    