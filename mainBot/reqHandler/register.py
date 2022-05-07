from linebot.models import TextSendMessage

from mainBot.models import User_Info, License_Key

#handle regist
def regist(usrMsgText , uid, usrName):
    message = []

    if(usrMsgText[1:3] == '註冊'):
        licenseKey = usrMsgText[3:].replace(' ', '')

        if(License_Key.objects.filter(licenseKey=licenseKey).exists() == True):
            User_Info.objects.create(uid=uid, licenseKey=licenseKey)
            License_Key.objects.filter(licenseKey=licenseKey).delete()
            resMsgText = usrName + '成功註冊'
            message.append(TextSendMessage(text=resMsgText))

        elif(len(licenseKey) == 0):
            resMsgText = '未輸入任何License key'
            message.append(TextSendMessage(text=resMsgText))

        else:
            resMsgText = 'License key錯誤'
            message.append(TextSendMessage(text=resMsgText))

    else:
        resMsgText = usrName + '您好\n系統偵測到您並未註冊帳號\n\n若要註冊請輸入：\n！註冊+您的License Key'
        message.append(TextSendMessage(text=resMsgText))

    return message

