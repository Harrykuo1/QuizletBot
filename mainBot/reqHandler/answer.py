import socket
from linebot.models import TextSendMessage, ImageSendMessage
from decouple import config

from mainBot.models import label_url, global_label_url


def findLabel(labelName, uid):
    if(global_label_url.objects.filter(labelName=labelName).exists() == True):
        globalLabels = global_label_url.objects.filter(labelName=labelName)
        for labelItem in globalLabels:
            labelUrl = labelItem.url
        return labelUrl
    elif(label_url.objects.filter(labelName=labelName, uid=uid).exists() == True):
        labels = label_url.objects.filter(labelName=labelName, uid=uid)
        for labelItem in labels:
            labelUrl = labelItem.url
        return labelUrl
    else:
        raise ValueError('No label')

def arrToStr(arr):
    string = ''
    for i in arr:
        string += str(i)+' '
    return string

def findAns(reqMsg, uid):
    message = []
    if(reqMsg[0] == ' '):
        reqMsg = reqMsg[1:]
    reqArr = reqMsg.split()
    if(len(reqArr) < 2):
        resMsgText = 'Syntax Error!'
        message.append(TextSendMessage(text=resMsgText))
    else:
        try:
            url = findLabel(reqArr[0], uid)
        except:
            resMsgText = 'No label!'
            message.append(TextSendMessage(text=resMsgText))
            return message

        reqArr[0] = url
        reqMsg = arrToStr(reqArr)
        res = reqAns(reqMsg)
        message.extend(res)

    return message


def reqAns(reqMsg):
    webhookUrl = config('webhookUrl')
    photoFolder = '/static/photo/'
    message = []
    HOST = 'quizlet'
    PORT = 7777
    clientMessage = reqMsg

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())

    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)

    resMsgText = 'Receive: ' + serverMessage
    serverMessageArr = list(map(int, serverMessage.split()))
    for item in serverMessageArr:
        message.append(ImageSendMessage(original_content_url=webhookUrl+photoFolder+str(item)+'.png', preview_image_url=webhookUrl+photoFolder+str(item)+'.png'))
    
    #resMsgText = 'Search over!'
    #message.append(TextSendMessage(text=resMsgText))
    client.close()
    return message

