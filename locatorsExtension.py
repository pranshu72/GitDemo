from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

driver.get('https://rahulshettyacademy.com/client')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('demo@gmail.com')  # //parent/child/grandchild -- XPATH
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys('Hello@1234')  # parent child:nth-child() grandchild -- CSS
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(3) input').send_keys('Hello@1234')
driver.find_element(By.XPATH, '//form/div[4]/button').click()
driver.find_element(By.LINK_TEXT, 'Login').click()

driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys('Hello@1234')
driver.find_element(By.CSS_SELECTOR, 'input[id=login]').click()
