from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://quotes.toscrape.com/')
print(type(driver.find_element_by_css_selector('.text')))
print(driver.find_element_by_css_selector('.text').text)

print('--------------------')
print(type(driver.find_elements_by_css_selector('.text')))
for tag in driver.find_elements_by_css_selector('.text'):
    print(tag.text)

driver.quit()