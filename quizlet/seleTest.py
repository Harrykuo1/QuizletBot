from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver.v2 as uc

import time

#time.sleep(10000)
url = 'https://quizlet.com/explanations/textbook-solutions/university-calculus-3rd-edition-9780134175706'

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

"""cookies = browser.get_cookies()
print(f"main: cookies = {cookies}")
browser.delete_all_cookies()"""

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, version_main=94)
driver.get(url)
driver.save_screenshot('photo/' + str(7777777) + '.png')
time.sleep(10)
driver.save_screenshot('photo/' + str(8888888) + '.png')
time.sleep(1000)