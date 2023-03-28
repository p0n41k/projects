import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from log_and_pass import login, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



s = Service(executable_path='C:\\Users\\Nurmakhanov\\Desktop\\ccode\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

cookies_file = 'cookies.pkl'


def scroll_to_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ждем загрузки новых элементов
        time.sleep(4)

        # Проверяем, достигли ли мы конца страницы
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Функция для сохранения кук в файл
def save_cookies():
    with open(cookies_file, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

# Функция для загрузки кук из файла
def load_cookies():
    with open(cookies_file, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

try:
    # Открываем страницу с клиентами
    driver.get('https://obtelecom.megaplan.ru/deals/list/22/state:353')
    input('Сайт открыт, нажми enter чтоб продолжить')

    # Попытка загрузить куки
    try:
        load_cookies()
        input('Куки загружены, жми Enter чтоб перейти на сайт с клиентами')

        # Переходим на страницу с клиентами после загрузки кук
        driver.get('https://obtelecom.megaplan.ru/deals/list/22/state:353')
        input('Мы перешли на сайт с клиентами')

        # Проверяем, успешно ли загружены куки
        login_test = driver.find_element(By.PARTIAL_LINK_TEXT, 'Подключен')
        input('Элемент найден, куки успешно загружены. Нажми Enter.')

    except:
        input('Что-то пошло не так, авторизация через логин и пароль')

        # Процесс авторизации, если загрузка кук не удалась
        login_inp = driver.find_element(By.ID, 'login')
        login_inp.clear()
        login_inp.send_keys(login)

        pass_inp = driver.find_element(By.ID, 'password')
        pass_inp.clear()
        pass_inp.send_keys(password)

        login_butt = driver.find_element(By.CLASS_NAME, 'button-text').click()
        input('Нажми Enter, чтобы продолжить.')

        # Переходим на страницу с клиентами после авторизации
        driver.get('https://obtelecom.megaplan.ru/deals/list/22/state:353')

    # Сохраняем куки после успешной авторизации или загрузки
    save_cookies()
    input('Куки сохранены успешно, нажми Enter.')

    # Создаем объект WebDriverWait для явного ожидания появления элементов на странице
    wait = WebDriverWait(driver, 10)

    # Прокручиваем страницу до конца
    scroll_to_end(driver)


    # Создаем файл для записи данных о клиентах
    with open("client_data.txt", "w", encoding="utf-8") as client_file:
        # Получаем данные о клиентах
        client_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody.CSmartTableBody > tr.J14y9he5YhU9OZvWjEee.T3Rop4pTAAEZzcwNbGaN')))

    for element in client_elements:
         client_info = element.text
         with open("client_data.txt", "a", encoding="utf-8") as client_file:
            client_file.write(f"{client_info}\n")
            client_file.write("---\n")

    input('enter для продолжения')



    '''
    место где данные приведены в готовый вид для рассылки

    место где производиться рассылка с помощью main.py
    '''

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()


