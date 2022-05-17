from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from mainBot.models import user_info, license_key

from mainBot.reqHandler.register import *
from mainBot.reqHandler.label import *
from mainBot.reqHandler.help import *


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
                usrName = profile.display_name
                usrMsgText = event.message.text
                message = []

                # 是否為指令
                if(usrMsgText[0] != '!' and usrMsgText[0] != '！'):
                    continue

                # 幫助
                if(usrMsgText[1:3] == '幫助'):
                    res = welcomeHelp()
                    message.extend(res)

                    res = funcHelp()
                    message.extend(res)

                # 未註冊
                elif (user_info.objects.filter(uid=uid).exists() == False):
                    res = regist(usrMsgText, uid, usrName)
                    message.extend(res)

                # 已註冊
                elif (user_info.objects.filter(uid=uid).exists() == True):
                    if(usrMsgText[1:3] == '註冊'):
                        message.append(TextSendMessage(text='請勿重複註冊'))
                    elif(usrMsgText[1:5] == '新增標籤'):
                        res = createLabel(usrMsgText, uid)
                        message.extend(res)
                    elif(usrMsgText[1:5] == '查詢標籤'):
                        res = listLabel(usrMsgText, uid)
                        message.extend(res)
                    elif(usrMsgText[1:5] == '刪除標籤'):
                        res = delLabel(usrMsgText, uid)
                        message.extend(res)
                    elif(usrMsgText[1:3] == '答案'):
                        res = findAns(usrMsgText[3:], uid)
                        message.extend(res)
                    


                line_bot_api.reply_message(event.reply_token, message)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
