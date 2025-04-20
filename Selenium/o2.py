from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://www.lazada.vn/products/chi-giao-trong-ban-kinh-15km-thung-sua-chua-uong-probi-it-duong-chai-130ml-24-chaithung-yogurt-i2756708-s3347924.html?scm=1007.17760.398138.0&pvid=262911a0-5998-41b4-bd40-4f984e348ab9&search=flashsale&spm=a2o4n.homepage.FlashSale.d_2756708")

driver.set_page_load_timeout(360)

time.sleep(5)

driver.execute_script("window.scroll(0, document.body.scrollHeight*0.6)")

# btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located(By.CSS_SELECTOR, "#module_product_review > div > div > div:nth-child(3) > div.next-pagination.next-pagination-normal.next-pagination-arrow-only.next-pagination-medium.medium.review-pagination > div > button.next-btn.next-btn-normal.next-btn-medium.next-pagination-item.next"))

while True:
    listCmt = driver.find_elements(By.CSS_SELECTOR, ".mod-reviews > div > .item-content > .content")
    for x in listCmt:
        print(x.text)
    next_btn = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((
                By.CSS_SELECTOR,
                "button.next-btn.next-btn-normal.next-btn-medium.next-pagination-item.next"
            ))
        )

    if next_btn.get_attribute("disabled"):
        print("Đã đến trang cuối.")
        break

    next_btn.click()
    time.sleep(2)

