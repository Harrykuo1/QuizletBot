from linebot.models import TextSendMessage

def welcomeHelp():
    emoji = [
        {
            "index": 14,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "009"
        },
        {
            "index": 41,
            "productId": "5ac21a18040ab15980c9b43e",
            "emojiId": "003"
        }
    ]

    message = []
    with open('/app/mainBot/textFile/welcomeHelp.txt', 'r') as f:
        resMsgText = f.read()
    message.append(TextSendMessage(text=resMsgText, emojis=emoji))
    return message

def funcHelp():
    message = []
    with open('/app/mainBot/textFile/funcHelp.txt', 'r') as f:
        resMsgText = f.read()
    message.append(TextSendMessage(text=resMsgText))
    return message