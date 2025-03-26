from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://dhthanhit.pythonanywhere.com/")

inp = driver.find_element(By.CSS_SELECTOR, 'form > input')
inp.send_keys('i')
btn = driver.find_element(By.CSS_SELECTOR, 'form > button')
btn.click()
driver.set_page_load_timeout(360)
products = driver.find_elements(By.CSS_SELECTOR, '.card')
for x in products:
    title = x.find_element(By.TAG_NAME, 'h4')
    print(title.text)

btnDetails = driver.find_elements(By.CSS_SELECTOR, '.card-body > a.btn.btn-primary')
url = [x.get_attribute('href') for x in btnDetails]
for b in url:
    driver.get(b)
    print('Comment')
    listCmt = WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'list-group-item')))
    for c in listCmt:
        content = c.find_element(By.CSS_SELECTOR, " div.col-md-11.col-sm-8 > p").text
        user = c.find_element(By.CSS_SELECTOR, "small > span:nth-child(2)").text
        print(f'{user}: {content}')
    print('=======')
driver.quit()