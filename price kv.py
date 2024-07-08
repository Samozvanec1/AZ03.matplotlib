import csv

def clean_price(price):

    return int(price.replace(' ₽/мес.', '').replace(' ', ''))

input_file = 'prices.csv' # входной файл с ценами (ссылка)
output_file = 'clean_prices.csv'  # выходной файл с очищенными ценами

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8' ) as outfile:
    with open(output_file, 'w', newline='') as csv_out_file:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader) # пропускаем первую строку с заголовками (названия столбцов)
        writer.writerow(header) # записываем новые названия столбцов в первую строку

        for row in reader: # обрабатываем остальные строки
            clean_row = clean_price(row[0]) # очищаем цену с помощью функции clean_price и записываем в новую строку
            writer.writerow([clean_row]) # записываем очищенную цену в новую строку

print(f"Обработанные данные сохранены в {output_file}")