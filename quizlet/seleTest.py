from selenium import webdriver
import time
#time.sleep(10000)
url = 'https://quizlet.com/explanations/textbook-solutions/university-calculus-3rd-edition-9780134175706'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1000)