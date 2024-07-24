from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

# Initialize the driver
driver = init_driver()

# List to hold all train data
train_data = []

# Total number of pages
total_pages = 227

# Loop through each page
for page in range(1, total_pages + 1):
    url = f"https://etrain.info/list/PASS-TRAINS?page={page}"
    driver.get(url)
    time.sleep(2)  # wait for the page to load

    # Extract data for the current page
    rows = driver.find_elements(By.XPATH, './/tr[@class="odd"] | .//tr[@class="even"]')
    
    for row in rows:
        train_number = row.find_element(By.XPATH, './td[1]/a').text
        train_name = row.find_element(By.XPATH, './td[2]/a').text
        from_station = row.find_element(By.XPATH, './td[3]').text
        to_station = row.find_element(By.XPATH, './td[4]').text
        
        data = {
            'Train Number': train_number,
            'Train Name': train_name,
            'From Station': from_station,
            'To Station': to_station
        }
        print(data)  # Print to terminal
        train_data.append(data)

# Close the driver
driver.quit()

# Save data to CSV file
csv_file = 'train_data.csv'
csv_columns = ['Train Number', 'Train Name', 'From Station', 'To Station']

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in train_data:
            writer.writerow(data)
    print(f"Data has been successfully written to {csv_file}")
except IOError:
    print("I/O error")
