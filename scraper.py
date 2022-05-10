from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configparser
import time
import traceback

configuration = configparser.ConfigParser()

try:
    if not configuration.read("config.ini"):
        raise FileNotFoundError

    d2lUsername = configuration['Authentication']['username']
    d2lPassword = configuration['Authentication']['password']

except FileNotFoundError:
    print("[Error] config.ini not found - please recreate it from the template")
    exit()

except KeyError:
    traceback.print_exc()
    print("[Error] config.ini may be corrupt or missing necessary settings - please recreate it from the template")
    exit()


with webdriver.Firefox() as driver:

    waitTen = WebDriverWait(driver, 10)
    
    driver.get("https://www.fanshaweonline.ca")

    unameElement = waitTen.until(EC.presence_of_element_located((By.ID, "username")))
    passElement = driver.find_element(By.ID, "password")

    unameElement.send_keys(d2lUsername)
    passElement.send_keys(d2lPassword)
    driver.find_element(By.NAME, "_eventId_proceed").click()

    waitTen.until(EC.title_is("Homepage - Fanshawe College"))
    

    driver.get("https://www.fanshaweonline.ca/d2l/lms/email/frame_list_mail.d2l?ou=29533&d2l_body_type=1&type=1&fk=0")
    emailTable = waitTen.until(EC.presence_of_element_located((By.XPATH, "//table[@id='z_f']/tbody")))


    messages = emailTable.find_elements(By.XPATH, ".//*[contains(@class, 'd2l-link')]")
    
    for i in messages:
        print(i.get_attribute('id'), i.get_attribute('title'))