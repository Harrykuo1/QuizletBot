import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service

def antiBan():
    time.sleep(1)

class quizletEngine:
    def __init__(self, account, passwd) -> None:
        self.account = account
        self.passwd = passwd
        self.loginUrl = 'https://quizlet.com/zh-tw'
        self.photoID = 100000000
        self.setup()
        try:
            self.login()
        except:
            print("Already Login finish")

    def checkPhotoID(self):
        if(self.photoID > 999999999):
            self.photoID = 100000000

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
        chrome_options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')

        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, version_main=94)

    def login(self):
        self.driver.get(self.loginUrl)
        self.driver.save_screenshot('photo/' + str(1) + '.png')
        self.driver.find_element(By.CLASS_NAME, "SiteNavLoginSection-loginButton").click()
        antiBan()
        self.driver.find_element(By.ID, "username").send_keys(self.account)
        antiBan()
        self.driver.find_element(By.ID, "password").send_keys(self.passwd)
        antiBan()
        #self.driver.find_element(by=By.CSS_SELECTOR, value="[aria-label=Exit]").click()
        #antiBan()
        self.driver.find_elements(by=By.CSS_SELECTOR, value="[aria-label=登入]")[1].click()
        antiBan()

        print("Login finish")

    def browsePage(self, url, bigChapter, smallChapter, questionList):
        photoIDArr = []
        #try:
        for questionIndex in questionList:
            print(bigChapter, smallChapter, questionIndex, end="\n")
            self.driver.get(url)
            self.driver.find_element(by=By.CSS_SELECTOR, value="[aria-label=第"+str(bigChapter)+"章]").click()
            antiBan()

            smallChapterList = self.driver.find_elements(by=By.CSS_SELECTOR, value="[aria-label^=第"+str(bigChapter)+"]")
            smallChapterList[smallChapter-1+1].click()
            antiBan()

            tmpRoot = self.driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid=TextbookTableOfContentsChapterMenu]")
            root = tmpRoot[bigChapter-1].find_element(by=By.CSS_SELECTOR, value="div>div>div>div>div:nth-child(2)>div>div>div:nth-child(%s)>span>a>span" %questionIndex)
            antiBan()

            root.click()
            antiBan()

            res = self.screenShot()
            photoIDArr.append(res)
        
        return photoIDArr
        #except:
            #self.driver.save_screenshot('photo/' + str('error') + '.png')
            


    def screenShot(self):
        try:
            js="var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            time.sleep(2)

            self.driver.find_element(by=By.CSS_SELECTOR, value="[aria-label=顯示所有步驟]").click()
            antiBan()

            js="var q=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
        except:
            pass
        time.sleep(2)
        res = self.photoID
        self.driver.save_screenshot('photo/' + str(self.photoID) + '.png')
        self.photoID+=1
        self.checkPhotoID()
        time.sleep(2)
        return res