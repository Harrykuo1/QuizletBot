from linebot.models import TextSendMessage

from mainBot.models import Label_Url

def funcHelp():
    message = []
    with open('/app/mainBot/textFile/funcHelp.txt', 'r') as f:
        resMsgText = f.read()
    message.append(TextSendMessage(text=resMsgText))
    return message

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
            resMsgText = '標籤'+msgArr[1]+'登記成功'
            message.append(TextSendMessage(text=resMsgText))

    return message


