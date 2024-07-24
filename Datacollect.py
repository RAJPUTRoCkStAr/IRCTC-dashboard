import time
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
################################################################
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver
def convert_to_hours(minutes):
    try:
        minutes = int(minutes)
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours}h {remaining_minutes}m"
    except ValueError:
        return minutes
    
def fill_missing_data(row_data):
    return ['None' if cell == '' else cell for cell in row_data]

def make_column_headers_unique(headers):
    seen = {}
    unique_headers = []
    for header in headers:
        if header not in seen:
            seen[header] = 0
            unique_headers.append(header)
        else:
            seen[header] += 1
            unique_headers.append(f"{header}_{seen[header]}")
    return unique_headers
################################################################
## making all the functions 
@st.cache_data(show_spinner=False)
def train_running_status(trains_no, trains_date):
    driver = init_driver()
    url = "https://indianrailways.info/train_running_status/"
    driver.get(url)
    trains_num = driver.find_element(By.ID, "train_no")
    trains_num.send_keys(trains_no)
    train_date = driver.find_element(By.ID, "run_day")
    train_date.send_keys(trains_date.strftime("%Y-%m-%d"))
    trains_num.send_keys(Keys.ENTER)
    try:
        table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-striped.table-bordered"))
        )
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_data = [header.text for header in headers]
        table_data = [header_data]
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                row_data = []
                for i, cell in enumerate(cells):
                    text = cell.text
                    if 2 <= i <= 17:    
                        text = convert_to_hours(text)
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_data.append(row_data)
        
        if len(table_data) == 1:
            table_data.append(['1'])
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        return df
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)
def train_running_history(trainh_no):
    driver = init_driver()
    url = "https://indianrailways.info/train_running_history/"
    driver.get(url)
    trainh_num = driver.find_element(By.ID, "train_no")
    trainh_num.send_keys(trainh_no)
    trainh_num.send_keys(Keys.ENTER)
    try:
        table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-striped.table-bordered"))
        )
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_data = [header.text for header in headers]
        header_data = make_column_headers_unique(header_data)  # Ensure unique column names
        table_data = [header_data]
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                row_data = []
                for i, cell in enumerate(cells):
                    text = cell.text
                    if 2 <= i <= 17:
                        text = convert_to_hours(text)
                    if text == '' or text.lower() == 'null':
                        text = '✅'
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_data.append(row_data)
                
        if len(table_data) == 1:
            table_data.append(['✅' for _ in header_data])
        
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        return df
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)
def importanst():
    driver = init_driver()
    url = "https://indianrailways.info/important_stations_and_trains/"
    driver.get(url)
    try:
        train_numbers = driver.find_elements(By.CLASS_NAME, "imp-train-number.white-text")
        train_names = driver.find_elements(By.CLASS_NAME, "imp-train-name.blue-text")
        train_number_texts = [train_number.text for train_number in train_numbers]
        train_name_texts = [train_name.text for train_name in train_names]
        return train_number_texts, train_name_texts
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)
def faredetails(fairdet_no, arr_st, dep_st):
    driver = init_driver()
    url = "https://indianrailways.info/fare_enquiry/"
    driver.get(url)
    trainh_num = driver.find_element(By.ID, "train_no")
    trainh_num.send_keys(fairdet_no)
    from_station_code = driver.find_element(By.ID, "from_station_code")
    from_station_code.send_keys(arr_st)
    to_station_code = driver.find_element(By.ID, "to_station_code")
    to_station_code.send_keys(dep_st)
    to_station_code.send_keys(Keys.ENTER)
    
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-striped.table-bordered"))
        )
        tables = driver.find_elements(By.CSS_SELECTOR, ".table.table-striped.table-bordered")
        if len(tables) < 2:
            st.warning("Less than 2 tables found. Ensure the page is fully loaded and contains the expected content.")
            return pd.DataFrame(), pd.DataFrame()
        table_data_1, table_data_2 = [], []
        header_data_1, header_data_2 = [], []
        table_1 = tables[0]
        headers_1 = table_1.find_elements(By.TAG_NAME, 'th')
        header_data_1 = [header.text for header in headers_1]
        rows_1 = table_1.find_elements(By.TAG_NAME, 'tr')
        for row in rows_1[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text for cell in cells]
            table_data_1.append(row_data)
        table_2 = tables[1]
        headers_2 = table_2.find_elements(By.TAG_NAME, 'th')
        header_data_2 = [header.text for header in headers_2]
        rows_2 = table_2.find_elements(By.TAG_NAME, 'tr')
        for row in rows_2[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text for cell in cells]
            table_data_2.append(row_data)
        df1 = pd.DataFrame(table_data_1, columns=header_data_1) if header_data_1 else pd.DataFrame(table_data_1)
        df2 = pd.DataFrame(table_data_2, columns=header_data_2) if header_data_2 else pd.DataFrame(table_data_2)        
        return df1, df2
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)  
def traintimetable(traint_num):
    driver = init_driver()
    url = 'https://indianrailways.info/train_time_table/'
    driver.get(url)
    trains_num = driver.find_element(By.ID, "train_no")
    trains_num.send_keys(traint_num)
    trains_num.send_keys(Keys.ENTER)
    try:
        table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-striped.table-bordered"))
        )
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_data = [header.text for header in headers]
        table_data = [header_data]
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                row_data = []
                for i, cell in enumerate(cells):
                    text = cell.text
                    if i==6:    
                        text = convert_to_hours(text)
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_data.append(row_data)
        
        if len(table_data) == 1:
            table_data.append(['1'])
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        return df
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)
def allstation(train_codes):
    driver = init_driver()
    url = 'https://indianrailways.info/all_trains/'
    driver.get(url)
    trains_code = driver.find_element(By.ID, "station_code")
    trains_code.send_keys(train_codes)
    trains_code.send_keys(Keys.ENTER)
    try:
        table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 
            ".table.table-striped.table-bordered.orange-text-table"))
        )
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_data = [header.text for header in headers]
        table_data = [header_data]
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                row_data = []
                for i, cell in enumerate(cells):
                    text = cell.text
                    if i == 6:    
                        text = convert_to_hours(text)
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_data.append(row_data)
        
        if len(table_data) == 1:
            table_data.append(['1'])

        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        return df
    finally:
        driver.quit()

@st.cache_data(show_spinner=False)
def allTrains(train_code):
    driver = init_driver()
    url = 'https://indianrailways.info/all_trains/'
    driver.get(url)
    trained_code = driver.find_element(By.ID, "station_code")
    trained_code.send_keys(train_code)
    trained_code.send_keys(Keys.ENTER)
    try:
        table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 
            ".table.table-striped.table-bordered.sort_table.high-table"))
        )
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_data = [header.text for header in headers]
        table_data = [header_data]
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                row_data = []
                for i, cell in enumerate(cells):
                    text = cell.text
                    if i == 6:    
                        text = convert_to_hours(text)
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_data.append(row_data)
                
        if len(table_data) == 1:
            table_data.append(['1'])

        dfs = pd.DataFrame(table_data[1:], columns=table_data[0])
        return dfs
    finally:
        driver.quit() 

@st.cache_data(show_spinner=False)      
def pnrsta(pnr_no):
    url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"
    querystring = {"pnrNumber":pnr_no}
    headers = {
	"x-rapidapi-key": "df3df38556mshaf705f750f27340p1e7b40jsncf340947eba6",
	"x-rapidapi-host": "irctc1.p.rapidapi.com"
}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
@st.cache_data(show_spinner=False)
def seat_avail(from_st, to_st, date):
    driver = init_driver()
    url = f'https://www.confirmtkt.com/rbooking-d/trains/from/{from_st}/to/{to_st}/{date}'
    driver.get(url)
    data = []
    try:
        wait = WebDriverWait(driver, 2)
        names = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="name"]')))
        departure_times = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="trainTime"]/span[1]')))
        arrival_times = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="trainTime"]/span[5]')))
        durations = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class="duration"]')))
        class_types = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="avail-cls"]/span[1]')))
        prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="avail-cls"]/span[2]')))
        predictions = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="prediction"]/span')))
        statuses = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="availability"]/span')))   
        num_trains = min(len(names), len(departure_times), len(arrival_times), len(durations))
        for i in range(num_trains):
            train_data = {
                "Train": names[i].text if i < len(names) else "N/A",
                "Departure Time": departure_times[i].text if i < len(departure_times) else "N/A",
                "Arrival Time": arrival_times[i].text if i < len(arrival_times) else "N/A",
                "Duration": durations[i].text if i < len(durations) else "N/A",
                "Classes": []
            }
            start_index = i * 5
            end_index = start_index + 5
            for j in range(start_index, min(end_index, len(class_types))):
                class_info = {
                    "Class": class_types[j].text if j < len(class_types) else "N/A",
                    "Price": prices[j].text if j < len(prices) else "N/A",
                    "Prediction": predictions[j].text if j < len(predictions) else "N/A",
                    "Status": statuses[j].text if j < len(statuses) else "N/A"
                }
                train_data["Classes"].append(class_info)
            data.append(train_data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    dfs = []
    for train in data:
        flat_data = []
        for cls in train["Classes"]:
            flat_data.append({
                "Train": train["Train"],
                "Departure Time": train["Departure Time"],
                "Arrival Time": train["Arrival Time"],
                "Duration": train["Duration"],
                "Class": cls["Class"],
                "Price": cls["Price"],
                "Prediction": cls["Prediction"],
                "Status": cls["Status"]
            })
        df = pd.DataFrame(flat_data)
        dfs.append(df)
    return dfs

@st.cache_data(show_spinner=False)
def trainbtst(fromsta,tosta):
    driver = init_driver()
    url = f'https://indianrailways.info/trains_between_stations/'
    driver.get(url)
    from_stati = driver.find_element(By.ID, "from_station_code")
    from_stati.send_keys(fromsta)
    to_stati = driver.find_element(By.ID, "to_station_code")
    to_stati.send_keys(tosta)
    from_stati.send_keys(Keys.ENTER)
    try:
        tables = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-striped.table-bordered"))
        )
        headerses = tables.find_elements(By.TAG_NAME, 'th')
        header_datas = [header.text for header in headerses]
        table_datas = [header_datas]
        rowss = tables.find_elements(By.TAG_NAME, 'tr')
        for row in rowss[1:]:
            cellss = row.find_elements(By.TAG_NAME, 'td')
            if cellss:
                row_data = []
                for i, cell in enumerate(cellss):
                    text = cell.text
                    if 2 <= i <= 17:    
                        text = convert_to_hours(text)
                    row_data.append(text)
                row_data = fill_missing_data(row_data)
                table_datas.append(row_data)
        
        if len(table_datas) == 1:
            table_datas.append(['1'])
        df = pd.DataFrame(table_datas[1:], columns=table_datas[0])
        return df
    finally:
        driver.quit()