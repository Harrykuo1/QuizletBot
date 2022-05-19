import os
import sys
import socket
import time
from quizletEngine import *
from decouple import config

account = config('quizletUser')
passwd = config('quizletPasswd')

#myEngine = quizletEngine(account, passwd)
#myEngine.browsePage(url, bigChapter, smallChapter, questionList)

HOST = '0.0.0.0'
PORT = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    print('Client message is:', clientMessage)

    serverMessage = clientMessage
    conn.sendall(serverMessage.encode())
    conn.close()
    
