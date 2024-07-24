from selenium import webdriver
from selenium.webdriver.common.by import By

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver
pageno = [pageno in range 230]
driver = init_driver()
url = f"https://etrain.info/list/PASS-TRAINS?page={pageno}"
driver.get(url)
try:
    trainno = driver.find_element(By.XPATH, './/tr[@class="odd lighthead bx0_bgm dborder"]/td').text
    print("PNR Number:", trainno)
    trainn = driver.find_element(By.XPATH, './/div[@class="pas-chart"]').text
    print("Chart Status:", trainn)
    ftrain = driver.find_element(By.XPATH, './/div[@class="pas-chart"]').text
    print("Chart Status:", ftrain)
    ttrain = driver.find_element(By.XPATH, './/div[@class="pas-chart"]').text
    print("Chart Status:", ttrain)
finally:
    driver.quit()
