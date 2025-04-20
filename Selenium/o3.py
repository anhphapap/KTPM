from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()

driver.get("https://www.sendo.vn/may-hut-chan-khong-mini-cao-cap-kiem-han-mieng-tui-vacuum-sealer-tang-kem-10-tui-102897685.html?source_block_id=feed&source_page_id=home&source_info=desktop2_60_1745119338186_8f97790f-a001-4ea7-bbe0-554f4a997bd4_-1_ishyperhome0_0_97_9_-1")

driver.set_page_load_timeout(360)

time.sleep(2)

driver.execute_script("window.scroll(0, document.body.scrollHeight*0.7)")

time.sleep(2)

while(True):
    listCmt = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#id-danh-gia div._39ab-_2vzod > p"))) 
    for x in listCmt:
        print(x.text)
    btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "ul.d7ed-EqmQtV > li:last-child > button")))
    driver.execute_script("arguments[0].scrollIntoView(true);", btn)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", btn)
    if btn.get_attribute("disabled"):
        break
    btn.click()
    time.sleep(2)