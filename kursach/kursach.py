# import csv



# with open("/Users/nikiforova.olesya/Desktop/сиаод/kursach/table.csv") as f:
#     arr = f.read().split("\n")

# data = []

# for line in arr:
#     row = line.split(';')
#     data.append(row)

# for line in data:
#   print(line) 

# n = len(arr)
# m = len(row)
# profit = 0

# for i in range(1, n):
#     profit += int(data[i][-1])

# print(profit)

# import csv

# # Создаем словарь для хранения данных о товарах
# products = {}

# # Открываем CSV-файл и считываем данные
# with open('/Users/nikiforova.olesya/Desktop/сиаод/kursach/table.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter=';', quotechar='"')
#     next(reader) # пропускаем заголовок
#     for row in reader:
#         # Получаем данные о продаже
#         order_number = row[0]
#         order_date = row[1]
#         product_name = row[2]
#         category = row[3]
#         quantity = int(row[4])
#         price = float(row[5])
#         total_price = float(row[6])
#         # print(product_name)
        
#         # Рассчитываем общую выручку магазина
#         if category not in products:
#             products[category] = {'revenue': 0, 'quantity': 0}
#         products[category]['revenue'] += total_price
#         for product in products:
#             products[product]['revenue'] = products[product]['price'] * products[product]['quantity']
        
#         # Находим товар, который был продан наибольшее количество раз
#         if product_name not in products:
#             products[product_name] = {'quantity': 0}
#         products[product_name]['quantity'] += quantity
        
# # Находим товар, который принес наибольшую выручку
# max_revenue_product = max(products, key=lambda x: products[x]['revenue'])

# # Формируем отчет
# total_revenue = sum(product['revenue'] for product in products.values())
# report = f"Total revenue: ${total_revenue:.2f}\n\nProduct sales:\n"
# for product_name, product_data in products.items():
#     revenue = product_data['revenue']
#     quantity = product_data['quantity']
#     sales_share = revenue / total_revenue * 100
#     report += f"{product_name}: ${revenue:.2f} ({quantity} units, {sales_share:.2f}%)\n"
# report += f"\nBest-selling product: {max(products, key=lambda x: products[x]['quantity'])}\n"
# report += f"Highest revenue product: {max_revenue_product}"

# # Выводим отчет
# print(report)


import csv
from collections import defaultdict

with open('/Users/nikiforova.olesya/Desktop/сиаод/kursach/table.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sales = [row for row in reader]

total_revenue = sum(float(sale.get('Общая стоимость', 0)) for sale in sales)
print('Общая выручка магазина: {:.2f}'.format(total_revenue))

best_seller = max(sales, key=lambda x: int(x.get('Количество продаж', 0)))
print('Самый популярный товар: {}'.format(best_seller.get('Название товара', 'Нет данных')))

if 'Название товара' in best_seller:
    print('Самый популярный товар: {}'.format(best_seller['Название товара']))
else:
    print('Самый популярный товар неизвестен')

most_profitable = max(sales, key=lambda x: float(x['Общая стоимость']))
print('Самый прибыльный товар: {}'.format(most_profitable['Название товара']))

report = defaultdict(int)
for sale in sales:
    report[sale['Название товара']] += int(sale['Количество продаж'])

print('Общая выручка магазина: {:.2f}'.format(total_revenue))
print('Количество продаж каждого товара:')
for item, count in report.items():
    revenue = sum(float(sale['Общая стоимость']) for sale in sales if sale['Название товара'] == item)
    percentage = (revenue / total_revenue) * 100
    print('{}: {} ({}%)'.format(item, count, round(percentage, 2)))
