import pandas as pd
import matplotlib.pyplot as plt

file_path = "clean_prices.csv" #путь к файлу с ценами
data = pd.read_csv(file_path) #считывает csv файл в pandas DataFrame (таблицу)

price = data["Price"] #выбирает столбец с ценами

plt.hist(price, bins=10, edgecolor="black") # можно изменить количество bin в зависимости от количества данных

plt.xlabel("Цена")
plt.ylabel("Частота встреч квартир с такой же ценой")
plt.title("Распределение цен")
plt.show()
