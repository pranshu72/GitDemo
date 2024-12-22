from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = webdriver.Edge()
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://capgemini.com")
driver.title
print(driver.title)
print(driver.current_url)
driver.get("https://www.capgemini.com/insights/")
driver.minimize_window()
driver.back()
driver.refresh()
# driver.forward()
# driver.close()
