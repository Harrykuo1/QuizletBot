from linebot.models import TextSendMessage

from mainBot.models import Label_Url

def createLabel(usrMsgText, uid):
    message = []
    msgArr = usrMsgText.split()

    if(len(msgArr) != 3):
        resMsgText = '指令格式錯誤，請重新輸入'
        message.append(TextSendMessage(text=resMsgText))

    else:
        if(Label_Url.objects.filter(uid=uid, labelName=msgArr[1]).exists() == True):
            resMsgText = '標籤已存在，請勿重複標記'
            message.append(TextSendMessage(text=resMsgText))
        else:
            Label_Url.objects.create(uid=uid, labelName=msgArr[1], url=msgArr[2])
            resMsgText = '標籤' + msgArr[1] + '登記成功'
            message.append(TextSendMessage(text=resMsgText))

    return message

def listLabel(usrMsgText, uid):
    message = []
    msgArr = usrMsgText.split()

    if(len(msgArr) != 1):
        resMsgText = '指令格式錯誤，請重新輸入'
        message.append(TextSendMessage(text=resMsgText))

    else:
        resMsgText = '您目前可用的標籤如下：\n'
        labelSet = set()

        labelQuery = Label_Url.objects.filter(uid=uid)
        for labelItem in labelQuery:
            labelSet.add(labelItem.labelName)

        labelQuery = Label_Url.objects.filter(uid='Global')
        for labelItem in labelQuery:
            labelSet.add(labelItem.labelName)

        index = 1
        for labelName in labelSet:
            resMsgText += str(index) + '. ' + labelName + '\n'
            index+=1

        message.append(TextSendMessage(text=resMsgText))

    return message



