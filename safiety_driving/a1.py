from config import yyour_ligin, yyour_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Nurmakhanov\\Desktop\\python scripts\\safiety_driving\\chromedriver.exe")

try:
    # open site
    driver.get(url="http://safety-driving.kz/personal/")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'USER_LOGIN')))
    time.sleep(0.5)

    # send user`s login
    username = driver.find_element(By.NAME,'USER_LOGIN')
    username.clear()
    username.send_keys(yyour_ligin)

    # send user`s password
    password = driver.find_element(By.NAME,'USER_PASSWORD')
    password.clear()
    password.send_keys(yyour_password)

    # click "login" for login
    login_button = driver.find_element(By.NAME,'Login').click() 
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-primary')))
    time.sleep(2)

    # open link with tests
    driver.get(url="http://safety-driving.kz/online2/exam/beta/#pages/tests.php")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-primary')))
    time.sleep(2)

    # start test
    start_test_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "bkt-start-test-button.btn.btn-primary.center-block")))
    time.sleep(2)

    start_test_button = driver.find_element(By.CLASS_NAME, "bkt-start-test-button.btn.btn-primary.center-block").click()
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-action="learn"]')))
    time.sleep(2)

    # select answer
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[data-action="browse"]').click()
            print("На все вопросы отвечены, надо получить данные")
            
            # найти родительский div
            parent_div = driver.find_element(By.CLASS_NAME, "bkt-questions-content")

            # найти все внутренние div
            inner_divs = parent_div.find_elements(By.XPATH, ".//div")

            html_codes = [div.get_attribute("outerHTML") for div in inner_divs]

            for i, code in enumerate(html_codes):
                soup = BeautifulSoup(code, 'html.parser')

            print(soup)
            break
        except:
            try:
                driver.find_element(By.CSS_SELECTOR, 'div[data-action="learn"]').click()
                WebDriverWait(driver, 1)
            
            except:
                keyboard.press("1")
                keyboard.release("1")
                WebDriverWait(driver, 1)
                keyboard.press("enter")
                keyboard.release("enter")
                WebDriverWait(driver, 1)
            
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
