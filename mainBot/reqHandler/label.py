from linebot.models import TextSendMessage

from mainBot.models import label_url, global_label_url

def createLabel(usrMsgText, uid):
    message = []
    msgArr = usrMsgText.split()

    if(len(msgArr) != 3):
        resMsgText = '指令格式錯誤，請重新輸入'
        message.append(TextSendMessage(text=resMsgText))

    else:
        if(label_url.objects.filter(uid=uid, labelName=msgArr[1]).exists() == True):
            resMsgText = '標籤已存在，請勿重複標記'
            message.append(TextSendMessage(text=resMsgText))
        else:
            label_url.objects.create(uid=uid, labelName=msgArr[1], url=msgArr[2])
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
        resMsgText = '您目前可用的標籤如下\n\n'
        resMsgText += '您的私人標籤：\n'

        myLabel = label_url.objects.filter(uid=uid)
        index = 1
        for labelItem in myLabel:
            resMsgText += str(index) + '. ' + labelItem.labelName + '\n'
            index+=1
        
        resMsgText += '\n預設標籤:\n'
        globalLabel = global_label_url.objects.filter()
        index = 1
        for labelItem in globalLabel:
            resMsgText += str(index) + '. ' + labelItem.labelName + '\n'
            index+=1
        message.append(TextSendMessage(text=resMsgText))

    return message

def delLabel(usrMsgText, uid):
    message = []
    msgArr = usrMsgText.split()

    if(len(msgArr) != 2):
        resMsgText = '指令格式錯誤，請重新輸入'
        message.append(TextSendMessage(text=resMsgText))

    else:
        if(label_url.objects.filter(uid=uid, labelName=msgArr[1]).exists() == True):
            label_url.objects.filter(uid=uid, labelName=msgArr[1]).delete()
            resMsgText = '標籤已刪除'
            message.append(TextSendMessage(text=resMsgText))
        else:
            resMsgText = '尚未登記此標籤'
            message.append(TextSendMessage(text=resMsgText))

    return message

