import time
import sys
import os
from decouple import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from twocaptcha import TwoCaptcha


def antiBan():
    time.sleep(1.2)

class ecourseEngine:
    def __init__(self, account, passwd) -> None:
        self.loginUrl = 'https://cas.ccu.edu.tw/login?service=https%3A%2F%2Fcas.ccu.edu.tw%2Foauth2.0%2FcallbackAuthorize%3Fclient_id%3DeCourse2%26redirect_uri%3Dhttps%253A%252F%252Fecourse2.ccu.edu.tw%252Fadmin%252Foauth2callback.php%26response_type%3Dcode%26client_name%3DCasOAuthClient'
        self.account = account 
        self.passwd = passwd
        self.setup()
        self.login()
        antiBan()
        self.driver.save_screenshot('success.png')
        """try:
            self.setup()
            self.login()
            antiBan()
            self.driver.save_screenshot('success.png')
        except:
            antiBan()
            self.driver.save_screenshot('error.png')"""


    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.user_data_dir = "temp/profile"
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1080') 
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument('--no-default-browser-check')

        chrome_options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
        #self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, version_main=94)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.delete_all_cookies()

    def login(self):
        self.driver.get(self.loginUrl)
        self.driver.find_element(By.ID, "username").send_keys(self.account)
        antiBan()
        self.driver.find_element(By.ID, "password").send_keys(self.passwd)
        antiBan()
        self.driver.save_screenshot('loginOver.png')
        self.crackAntiBot()

    def crackAntiBot(self):
        js = "document.getElementById('g-recaptcha-response').style.display='block'"
        self.driver.execute_script(js)
        self.driver.save_screenshot('gBlock.png')

        data_sitekey = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha"))).get_attribute("data-sitekey")
        api_key = config("apiKey")
        solver = TwoCaptcha(api_key)
        try:
            result = solver.recaptcha(
                sitekey=data_sitekey,
                url=self.loginUrl,
                action='login',
            )
            print(result["code"])
        except Exception as e:
            sys.exit(e)


        self.driver.find_element(By.ID, "g-recaptcha-response").send_keys(result["code"])
        antiBan()
        self.driver.save_screenshot('sendKey.png')
        antiBan()
        self.driver.find_element(By.NAME, "submit").click()

        time.sleep(3)

    def logout(self):
        pass
    def allScore(self):
        pass
    def partScore(self):
        pass
