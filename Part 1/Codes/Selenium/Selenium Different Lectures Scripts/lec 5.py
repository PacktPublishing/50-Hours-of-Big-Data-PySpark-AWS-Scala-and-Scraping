from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://quotes.toscrape.com/')
for div in driver.find_elements_by_css_selector('.quote'):
    print(div.find_element_by_css_selector('.text').text)
    print(div.find_element_by_css_selector('.author').text)
    print('----------------')




driver.quit()