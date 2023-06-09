import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='C:\\Users\\Nurmakhanov\\Desktop\\ccode\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:
    # Открыть WhatsApp Web
    driver.get('https://web.whatsapp.com/')
    input("Зайди в аккаунт WhatsApp Buisness, а затем нажми Enter")

    # Чтение переменных из файла
    with open('variables.txt',encoding='utf-8',) as f:
        variables = f.read
        variables = f.readlines()
    variables = [v.strip() for v in variables]

    # Найти элемент body
    body_element = driver.find_element(By.TAG_NAME, 'body')

    # Обработка переменных
    for var in variables:
        time.sleep(2)
        body_element.send_keys(Keys.ESCAPE)

        # Открыть чат с самим собой
        my_chat = driver.find_element(By.CLASS_NAME, 'tvf2evcx.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr').click()
        print("Чат с самим собой открыт")
        time.sleep(3)

        # Вставка текста в чат
        select_chat = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        select_chat.clear()
        select_chat.send_keys(var)
        print("текст вставлен")
        time.sleep(3)

        # Отправка сообщения
        select_chat.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # Выбор сообщения и переход в новый чат
        tap_mess = driver.find_element(By.PARTIAL_LINK_TEXT, var).click()
        time.sleep(3)
        enter_chat = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        enter_chat.send_keys(Keys.ENTER)
        time.sleep(2)
        body_element.send_keys(Keys.ESCAPE)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
