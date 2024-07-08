from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import csv
import matplotlib.pyplot as plt

def clean_price(price):
    return int(price.split("р")[0].replace(' ', ''))


url = "https://www.divan.ru/category/divany-i-kresla"

driver = webdriver.Firefox()
driver.set_page_load_timeout(5)
try:
   driver.get(url)
except:
   pass

prices = driver.find_elements(By.CLASS_NAME, 'pY3d2') # находит все элементы с ценой
clean_prices = []
with open('Divo_Divnoe.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])#записывает в первую строку названия столбцов (цена)

    for price in prices:
        clean_prices.append(clean_price(price.text))
        writer.writerow([clean_price(price.text)]) #записывает цену в первую строку

driver.quit() #закрывает браузер
plt.hist(clean_prices, bins=10, edgecolor="black") # можно изменить количество bin в зависимости от количества данных
plt.xlabel("Цена")
plt.ylabel("Частота встреч диванов с такой же ценой")
plt.title("Распределение цен")
plt.show()









