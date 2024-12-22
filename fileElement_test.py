import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

assert(driver.find_element(By.ID, 'autosuggest').get_attribute('value')) == 'India'
