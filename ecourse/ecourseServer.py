import os
import sys
import socket
import time
from ecourseEngine import *
from decouple import config

HOST = '0.0.0.0'
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    clientMessageArr = clientMessage.split()
    account = clientMessageArr[0]
    passwd = clientMessageArr[1]
    myEngine = ecourseEngine(account, passwd)
    if(len(clientMessageArr) == 2):
        myEngine.allScore()
        serverMessage = "OK"
    elif(len(clientMessageArr) == 3):
        pass
    else:
        serverMessage = "錯誤格式，請重新輸入"

    conn.sendall(serverMessage.encode())
    conn.close()
    
