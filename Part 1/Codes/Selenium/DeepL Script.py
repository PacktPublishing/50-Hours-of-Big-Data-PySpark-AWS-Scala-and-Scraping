from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

with open('input.txt','r') as f:
    text = f.read().strip()

driver.get('https://www.deepl.com/translator')
driver.find_element_by_css_selector('.dl_cookieBanner--buttonClose').click()
time.sleep(3)
driver.find_element_by_css_selector('.lmt__language_container_prim .lmt__language_select__opener').click()
time.sleep(3)
driver.find_element_by_css_selector('[dl-test="translator-lang-option-ru-RU"]').click()
time.sleep(3)
inputTextArea = driver.find_element_by_css_selector('.lmt__textarea')
inputTextArea.send_keys(text)
time.sleep(5)
driver.find_element_by_css_selector('.lmt__target_toolbar__save button').click()

# driver.quit()

