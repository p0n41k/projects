from config import yyour_ligin, yyour_password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import keyboard
import os
from bs4 import BeautifulSoup



driver = webdriver.Chrome(executable_path="C:\\Users\\Nurmakhanov\\Desktop\\python scripts\\safiety_driving\\chromedriver.exe")

try:
    # open site
    driver.get(url="https://wa.me/77021110710?text=Здравствуйте,%20Абдисадык!%0A%0AНапоминаем,%20что%20ежемесячное%20списание%20абонентской%20платы%20происходит%20каждое%201%20число%20месяца.%20Чтобы%20избежать%20перебоев%20в%20работе%20интернета,%20пожалуйста,%20заранее%20пополните%20свой%20лицевой%20счет.%20Пополнить%20лицевой%20счет%20можно%20следующим%20образом:%0A%0A1.%20Перейдите%20по%20ссылке:%0Ahttps://kaspi.kz/pay/ainaline%0A2.%20Введите%20ваш%20лицевой%20счет:%2020300003%0A3.%20Проверьте,%20совпадает%20ли%20адрес%20и%20ФИО%20с%20вашими%20данными%0A4.%20Оплатите%20сумму%0A%0AС%20уважением,%0AКоманда%20AinaLine")
    time.sleep(200)

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
    time.sleep(2)

    directory = "safiety_driving\\res_versions"
    if not os.path.exists(directory):
        os.makedirs(directory)

    result_versons = 1    
    
    while result_versons <= 2000:






        # open link with tests
        driver.get(url="http://safety-driving.kz/online2/exam/beta/#pages/tests.php")
        time.sleep(2)

        # start test
        start_test_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
        time.sleep(3)
        start_test_button = driver.find_element(By.CLASS_NAME, "bkt-start-test-button.btn.btn-primary.center-block").click()
        time.sleep(3)

        # select answer
        while True:
            def answer():
                try:
                    driver.find_element(By.CSS_SELECTOR, 'div[data-action="learn"]').click()
                    time.sleep(0.1)
                
                except:
                    keyboard.press("1")
                    keyboard.release("1")
                    keyboard.press("enter")
                    keyboard.release("enter")
            
            try:
                driver.find_element(By.CSS_SELECTOR, 'div[data-action="browse"]').click()
                print("На все вопросы отвечены, надо получить данные")
                
                # найти родительский div
                parent_div = driver.find_element(By.CLASS_NAME, "bkt-questions-content")

                # найти все внутренние div
                inner_divs = parent_div.find_elements(By.XPATH, ".//div")

                html_codes = [div.get_attribute("outerHTML") for div in inner_divs]
                result = ""
                for i, code in enumerate(html_codes):
                    soup = BeautifulSoup(code, 'html.parser')
                    result += str(soup)

                print(result)

                filename = 'version_{0}.txt'.format(result_versons)

                if os.path.exists(directory + filename):
                  result_versons += 1
                else:
                    with open(directory + filename, 'w', encoding='utf-8') as f:
                        f.write(result)
                break

                    

            except:
                answer()            
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
