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

sockFile = 'socket.sock'

try:
    os.unlink(sockFile)
    pass
except OSError:
    if os.path.exists(sockFile):
        raise
    pass

# 指定协议
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(sockFile)
# 监听
server.listen(1)
print("Prepare finish")
while True:
    clientsocket, address = server.accept()
    data = clientsocket.recv(1024)
    print(data)
    clientsocket.close()

    
