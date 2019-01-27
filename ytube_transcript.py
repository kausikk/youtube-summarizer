import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def get_audio(url):
    chrome_options = Options()  
    # chrome_options.add_argument('--headless')  
    driver = webdriver.Chrome(options=chrome_options)  

    result = ''
    driver.get("https://ytmp3.cc/")

    driver.find_element_by_id('input').send_keys(url)
    driver.find_element_by_id('submit').click()

    try:
        driver.implicitly_wait(5)
        result = driver.find_element_by_id('download').get_attribute('href')
    except Exception as e:
        print(e)
        result = 'No link found'
    
    driver.quit()
    print(result)

