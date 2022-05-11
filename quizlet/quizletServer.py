import os
import socket
import time
from quizletEngine import *
from decouple import config

sock_address = './socket.sock'
account = config('quizletUser')
passwd = config('quizletPasswd')

try:
    os.unlink(sock_address)
except OSError:
    if os.path.exists(sock_address):
        raise

"""url = 'https://quizlet.com/explanations/textbook-solutions/university-calculus-3rd-edition-9780134175706'
bigChapter =3
smallChapter = 5
questionList = [2, 3, 5, 7, 11]"""

myEngine = quizletEngine(account, passwd)
#myEngine.browsePage(url, bigChapter, smallChapter, questionList)
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(sock_address)
server.listen(20)
while True:
    clientSock, address = server.accept()
    reqMsg = clientSock.recv(1024)
    print('recieve: \n' + reqMsg.decode() + '\n')

    resMsg = 'hi'
    clientSock.send(resMsg.encode())
    clientSock.close()
