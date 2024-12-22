from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# options = Options()
# options.add_experimental_option('detach', True)
# chrome_driver = webdriver.Chrome()

service_obj = Service("C:/Users/pranshu/Downloads/edgedriver")
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com")

# driver.quit()
