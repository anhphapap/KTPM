from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.conferenceseries.com/past-conference-reports.php")

articles = driver.find_elements(By.CSS_SELECTOR, 'a.list-group-item.clearfix')
driver.set_page_load_timeout(360)
for x in articles:
    try:
        title = x.get_attribute('title')
        time = x.find_element(By.CSS_SELECTOR,'div:nth-child(2) > span')
        location = x.find_element(By.CSS_SELECTOR, 'div:nth-child(3)')
        print(title)
        print(time.text)
        print(location.text)
        print('=======')
    except:
        pass

print(driver.title)
driver.quit()