import cv2
import numpy as np
from PIL import Image
import pytesseract
from matplotlib import pyplot as plt

from linebot.models import TextSendMessage
from mainBot.models import image_cmd_tmp

from mainBot.reqHandler.answer import *

def imageCmd(reqMsg, uid):
    message = []
    if(reqMsg[0] == ' '):
        reqMsg = reqMsg[1:]
    reqArr = reqMsg.split()
    if(len(reqArr) != 2):
        resMsgText = 'Syntax Error!'
        message.append(TextSendMessage(text=resMsgText))
    else:
        if(image_cmd_tmp.objects.filter(uid=uid).exists() == True):
            cmdObj = image_cmd_tmp.objects.get(uid=uid)
            cmdObj.cmd = reqMsg
            cmdObj.save()
        else:
            image_cmd_tmp.objects.create(uid=uid, cmd=reqMsg)
        
        resMsgText = 'Please input image!'
        message.append(TextSendMessage(text=resMsgText))
    
    return message

def transImg(imgName):
    # Step1. 轉換為HSV
    img = cv2.imread('./static/clientImg/' + str(imgName))
    
    # Step1. 將圖片從BGR轉換為HSV
    hue_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Step2. 用顏色分割圖像
    low_range = np.array([0, 123, 100])
    high_range = np.array([5, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)

    # Step3. 形態學運算，膨脹 使紅色區域變為更加明顯 降低錯誤率
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2)), iterations=3)

    # Step4. Hough Circle 提取圖像中的圓形
    circles = cv2.HoughCircles(dilated, cv2.HOUGH_GRADIENT, 1, 100, param1=20, param2=20, minRadius=20, maxRadius=1000)

    circleS = circles.reshape(-1, 3)
    circleS = np.uint16(np.around(circleS))
            
    i = 1
    j = len(circles[0])
    #銳化用filter
    sharpen_filter = np.array([[-1, -1, -1], [-1, 10.5, -1], [-1, -1, -1]])

    T = []
    i = 1
    # Step5. 繪製    
    for k in circleS:
        cv2.circle(img, (k[0], k[1]), k[2], (0, 255, 0), 2)
        half_circle=int(k[2])-17
        crop_img = img[k[1]-half_circle:k[1]+half_circle, k[0]-half_circle:k[0]+half_circle]
        #cv2.imshow("cropped", crop_img)

        grayed_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) #灰階
        
        sharped_img = cv2.filter2D(grayed_img, -1, sharpen_filter)#銳化
        
        kernel = np.ones((3,3), np.uint8)
        img_denoising = cv2.morphologyEx(sharped_img, cv2.MORPH_OPEN, kernel)#降噪
        
        ret, bin_img = cv2.threshold(img_denoising, 127, 255, cv2.THRESH_BINARY)#二值化

        text = pytesseract.image_to_string(bin_img, lang='eng')#讀取數字

        T.append(text)

        file_name = str(i) + '.jpg'
        cv2.imwrite(file_name, bin_img)
        i += 1

    U = []
    V = []
    x = 0
    y = 0
    resArr = []
    #去除數字以外的，保留數字
    while x < len(T):
        U = list(T[x])
        while y < len(U):
            if U[y].isdigit():
                V.append(U[y])
                y += 1
            else:
                y += 1
        ans = "".join(V) #ans為所需數字
        resArr.append(int(ans))
        print(ans)
        V.clear()
        y = 0
        x += 1

    return resArr

def findAnsByImg(questionsArr, uid):
    message = []
    if(image_cmd_tmp.objects.filter(uid=uid).exists() == True):
        cmdObj = image_cmd_tmp.objects.get(uid=uid)
        reqMsg = cmdObj.cmd
        reqMsg += ' '
        for questionIndex in questionsArr:
            reqMsg += str(questionIndex) + ' '

        res = findAns(reqMsg, uid)
        message.extend(res)

    else:
        resMsgText = 'Please input chapter first!'
        message.append(TextSendMessage(text=resMsgText))
    return message



