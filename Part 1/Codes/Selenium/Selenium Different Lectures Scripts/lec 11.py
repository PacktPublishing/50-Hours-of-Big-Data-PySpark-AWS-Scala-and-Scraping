from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://quotes.toscrape.com/')

driver.find_element_by_css_selector('.header-box p a').click()
username = driver.find_element_by_css_selector('#username')
username.send_keys('ABC')
time.sleep(3)
password = driver.find_element_by_css_selector('#password')
password.send_keys('12345')
time.sleep(3)
driver.find_element_by_css_selector('[value="Login"]').click()

driver.quit()