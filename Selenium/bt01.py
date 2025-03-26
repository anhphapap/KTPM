from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://vnexpress.net/")

articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news.item-news-common')
driver.set_page_load_timeout(360)
for x in articles:
    try:
        title = x.find_element(By.CSS_SELECTOR,'h3 > a')
        des = x.find_element(By.CSS_SELECTOR,'.description > a')
        img = x.find_element(By.TAG_NAME, 'img')
        print(title.text)
        print(des.text)
        print(img.get_attribute('src'))
        print('=======')
    except:
        pass

print(driver.title)
driver.quit()