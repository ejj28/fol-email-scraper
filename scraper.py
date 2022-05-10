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

except:
    traceback.print_exc()
    exit()


with webdriver.Firefox() as driver:

    waitTen = WebDriverWait(driver, 10)
    
    driver.get("https://www.fanshaweonline.ca")

    unameElement = waitTen.until(EC.presence_of_element_located((By.ID, "username")))
    passElement = driver.find_element(By.ID, "password")

    unameElement.send_keys(d2lUsername)
    passElement.send_keys(d2lPassword)
    driver.find_element(By.NAME, "_eventId_proceed").click()

    time.sleep(60)