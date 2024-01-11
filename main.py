from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
b = []
u = 0
def prokrytka(skolko_nad):
    for i in range (1 , skolko_nad):
        time.sleep(1)
        scroll_vаlue = 350
        scroll_by = f'window.scrollBy(0, {scroll_vаlue});'
        driver.execute_script(scroll_by)
    all = driver.find_elements(By.CLASS_NAME, 'product-card__wrapper')
    return all
q = input('Что хотите запарстиь? ')

while all != b:
            u = u + 1
            url = f'https://www.wildberries.ru/catalog/0/search.aspx?page={u}&sort=popular&search={q}'
            options = webdriver.ChromeOptions()
            options.add_argument(f'user_agent = {UserAgent.random}')
            driver = webdriver.Chrome(options=options)
            f = 0
            try:
                driver.get(url=url)
                time.sleep(1)

                all = prokrytka(45)
                for i in all:
                        f = f + 1

                        if f <= 100:
                            i.click()
                            time.sleep(1)
                            header1 = driver.find_element(By.CLASS_NAME ,'product-page__header').text
                            header = header1.replace('\n', ' ')
                            print(header)
                            Cena_0 = driver.find_element(By.CLASS_NAME, 'price-block__final-price').text.replace('₽', '')
                            Cena = int(Cena_0.replace(" ", ""))
                            print(Cena)
                            opis = driver.find_element(By.CLASS_NAME, "collapsable__text").text.replace('\n', " ")
                            print(opis)

                            driver.find_element(By.CLASS_NAME, 'breadcrumbs__back').click()
                            time.sleep(1)

            except Exception as _ex:
                    print(_ex)



