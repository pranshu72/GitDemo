import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = Service("C:/Users/pranshu/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/')


time.sleep(2)


# Make sure it is .exe file


# Open a website
