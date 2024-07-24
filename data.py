import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    driver = webdriver.Chrome(options=options)
    return driver
driver = init_driver()
data = [] 
url = 'https://icf.indianrailways.gov.in/PB/pass/stations.html'
driver.get(url)
rows = driver.find_elements(By.XPATH, './/table//tr')
for row in rows:
    cells = row.find_elements(By.XPATH, './/th | .//td')
    cell_data = [cell.text for cell in cells]
    data.append(cell_data)
df = pd.DataFrame(data)
df.to_csv('train_availability.csv', index=False)
driver.quit()
print(df)
