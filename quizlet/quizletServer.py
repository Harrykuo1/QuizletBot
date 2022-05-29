import os
import sys
import socket
import time
from quizletEngine import *
from decouple import config

account = config('quizletUser')
passwd = config('quizletPasswd')

url = "https://quizlet.com/explanations/textbook-solutions/university-calculus-early-transcendentals-3rd-edition-9780321999573"
bigChapter = 3
smallChapter = 2
questionList = [2,3]
myEngine = quizletEngine(account, passwd)
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

    clientMessageArr = list(clientMessage.split())
    url = clientMessageArr[0]
    chapter = str(clientMessageArr[1])
    questionList = list(map(int, clientMessageArr[2:]))
    bigChapter, smallChapter =  map(int,chapter.split("-"))

    print('Client message is:', clientMessage)
    print("url: ", url)
    print("bigChapter : ", bigChapter)
    print("smallChapter: ", smallChapter)

    """url = "https://quizlet.com/explanations/textbook-solutions/university-calculus-early-transcendentals-3rd-edition-9780321999573"
    bigChapter = 3
    smallChapter = 2
    questionList = [2,3]"""



    res = myEngine.browsePage(url, bigChapter, smallChapter, questionList)
    serverMessage = ''
    for photoID in res:
        serverMessage += str(photoID) + ' '

    conn.sendall(serverMessage.encode())
    conn.close()
    
