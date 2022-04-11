from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://quotes.toscrape.com/page/9/')

while True:
    for div in driver.find_elements_by_css_selector('.quote'):
        print(div.find_element_by_css_selector('.text').text)
        print(div.find_element_by_css_selector('.author').text)

    try:
        driver.find_element_by_css_selector('.next a').click()
    except:
        break




driver.quit()