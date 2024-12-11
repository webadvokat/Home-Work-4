# %%
import json  #JSON

# Создаём словарь
purchases = {}

# Открываем файл purchase_log.txt и читаем построчно
with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        record = json.loads(line.strip())  # перевод строки в словарь
        purchases[record['user_id']] = record['category']  #наполняем словарь

#Выводим первые элементы словаря
for i, (user_id, category) in enumerate(purchases.items()):
    print(f"{user_id} '{category}'")
    if i == 1:  #стоп после двух строк
        break


# %%
import csv  #CSV

#Создаём файл funnel.csv
with open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    #Записываем CSV
    writer = csv.writer(funnel_file)
    writer.writerow(['user_id', 'source', 'category'])  #Название столбцов
    
    #Открываем visit_log (2).csv для построчного чтения
    with open('visit_log (2).csv', 'r', encoding='utf-8') as visit_file:
        reader = csv.reader(visit_file)
        next(reader)  #Пропускаем заголовок

        #Обрабатываем строки
        for row in reader:
            user_id, source = row
            category = purchases.get(user_id)  #Проверяем, есть ли покупка
            if category:  #Если есть категория, записываем в файл
                writer.writerow([user_id, source, category])

with open('funnel.csv', 'r', encoding='utf-8') as funnel_file:
    reader = csv.reader(funnel_file)
    for i, row in enumerate(reader):
        print(row)  #Выводим строки
        if i == 1:  #стоп после двух строк
            break




