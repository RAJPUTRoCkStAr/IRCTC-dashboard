import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver
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