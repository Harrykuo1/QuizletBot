import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def antiBan():
    time.sleep(1)

class quizletEngine:
    def __init__(self, account, passwd) -> None:
        self.account = account
        self.passwd = passwd
        self.loginUrl = 'https://quizlet.com/zh-tw'
        self.photoID = 100000000
        self.login()

    def checkPhotoID(self):
        if(self.photoID > 999999999):
            self.photoID = 100000000

    def login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

        self.driver.get(self.loginUrl)
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
        res = []
        for questionIndex in questionList:
            self.driver.get(url)
            self.driver.find_element(by=By.CSS_SELECTOR, value="[aria-label=第"+str(bigChapter)+"章]").click()
            header = self.driver.find_elements(By.CLASS_NAME, "twe4x3d")
            antiBan()

            allChild = header[bigChapter-1].find_elements(By.TAG_NAME, "button")
            allChild[smallChapter-1].click()
            antiBan()

            header = self.driver.find_elements(By.CLASS_NAME, "e1xvy4j")
            allChild = header[bigChapter-1].find_elements(By.CLASS_NAME, "e1nsy6m5")


            target = allChild[questionIndex-1].find_element(By.TAG_NAME, "span")
            target = target.find_element(By.TAG_NAME, "a")
            target.click()
            antiBan()

            self.screenShot()

    def screenShot(self):
        js="var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(2)

        self.driver.find_element(by=By.CSS_SELECTOR, value="[aria-label=顯示所有步驟]").click()
        antiBan()

        js="var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        time.sleep(2)

        self.driver.save_screenshot('photo/' + str(self.photoID) + '.png')
        self.photoID+=1
        self.checkPhotoID()
        time.sleep(2)