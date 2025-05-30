from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get("https://tiki.vn/ky-luat-ban-than-p190238356.html?spid=190238357")

driver.set_page_load_timeout(360)
driver.execute_script("window.scroll(0, 3600)")
listCmt = WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'review-comment__content')))
for x in listCmt:
    print(x.text)

driver.quit()