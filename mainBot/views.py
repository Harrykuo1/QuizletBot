from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from mainBot.models import User_Info, License_Key

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                uid = event.source.user_id
                profile = line_bot_api.get_profile(uid)
                userName = profile.display_name
                userMsgText = event.message.text
                message = []

                # 是否為指令
                if(userMsgText[0] != '！'):
                    continue

                # 幫助
                if(userMsgText == '！幫助'):
                    with open('/app/mainBot/textFile/help.txt', 'r') as f:
                        resMsgText = f.read()

                    message.append(TextSendMessage(text=resMsgText))

                # 未註冊
                elif (User_Info.objects.filter(uid=uid).exists() == False):
                    if(userMsgText[:3] == '！註冊'):
                        licenseKey = userMsgText[3:].replace(' ', '')

                        if(License_Key.objects.filter(licenseKey=licenseKey).exists() == True):
                            User_Info.objects.create(
                                uid=uid, licenseKey=licenseKey)
                            License_Key.objects.filter(
                                licenseKey=licenseKey).delete()
                            resMsgText = userName + '成功註冊'
                            message.append(TextSendMessage(text=resMsgText))
                        elif(len(licenseKey) == 0):
                            resMsgText = '未輸入任何License key'
                            message.append(TextSendMessage(text=resMsgText))
                        else:
                            resMsgText = 'License key錯誤'
                            message.append(TextSendMessage(text=resMsgText))

                    else:
                        resMsgText = userName + '您好\n系統偵測到您並未註冊帳號\n\n若要註冊請輸入：\n！註冊+您的License Key'
                        message.append(TextSendMessage(text=resMsgText))

                # 已註冊
                elif (User_Info.objects.filter(uid=uid).exists() == True):
                    resMsgText = userName + '已註冊過'
                    message.append(TextSendMessage(text=resMsgText))

                line_bot_api.reply_message(event.reply_token, message)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
