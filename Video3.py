from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import csv

# firefox_driver_path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
# service = Service(executable_path=firefox_driver_path)
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)

driver = webdriver.Firefox()

url = "https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"

driver.get(url) # открывает ссылку
time.sleep(5)

prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span") # находит все элементы с ценой

with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])#записывает в первую строку названия столбцов (цена)

    for price in prices:
        writer.writerow([price.text]) #записывает цену в первую строку

driver.quit()


