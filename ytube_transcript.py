import os
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

def get_audio(url):
    chrome_options = Options()  
    chrome_options.add_argument('--headless')  
    driver = webdriver.Chrome(options=chrome_options)  

    result = ''
    driver.get("https://ytmp3.cc/")

    driver.find_element_by_id('input').send_keys(url)
    driver.find_element_by_id('submit').click()

    try:
        result = wait_for_dl_link(driver)
    except Exception as e:
        print(e)
        result = 'No link found'
    
    driver.quit()
    return result

# Private helper
def wait_for_dl_link(driver):
    i = 0
    result = ''
    while i < 10 and result == '':
        i += 1
        time.sleep(1)
        result = driver.find_element_by_id('download').get_attribute('href')
    return result
