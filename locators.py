from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys('Rahul Shetty')
driver.find_element(By.NAME, 'email').send_keys('hello@gamil.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('12345')
# driver.find_element(By.ID, 'exampleFormControlSelect1').send_keys('Female')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again!")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# Static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)
# dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()  # syntax for XPATH- //tagname[@attribute = 'value]
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()  # syntax for CSS_SELECTOR- tagname[attribute = 'value]
msg = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(msg)
assert "Success" in msg
