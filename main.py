"""
Пример работы интернет-магазина

Этот скрипт демонстрирует основные функции системы интернет-магазина,
используя классы Product, Customer, Order и Discount.

Классы:
- Product: представляет товар с именем и ценой.
- Customer: представляет клиента интернет-магазина, который может иметь
один или несколько заказов.
- Order: представляет заказ, который может содержать несколько товаров.
- Discount: представляет систему скидок, которые могут применяться к
заказам.

Основной функционал:
1. Создание продуктов.
2. Создание клиентов.
3. Создание заказов.
4. Добавление заказов к клиентам.
5. Применение различных типов скидок к заказам.
6. Подсчет общей стоимости заказов с учетом скидок.
7. Вывод информации о клиентах, их заказах и итоговой стоимости.

Использование:
1. Инициализируйте продукты, указывая их имя и цену.
2. Создайте клиентов с их именами и добавьте их в общий список.
3. Создайте заказы и добавьте в них ранее созданные продукты.
4. Добавьте созданные заказы к соответствующим клиентам.
5. Создайте скидки и примените их к заказам, чтобы получить общую цену после
применения скидки.
6. Выведите информацию о клиентах и их заказах.
7. Подсчитайте общее количество заказов и общую стоимость всех заказов
для всех клиентов.

Примечание: Убедитесь, что все ваши модули (product.py, customer.py, order.py, discount.py)
находятся в одной директории при запуске этого скрипта.
"""

from classes.product import Product
from classes.customer import Customer
from classes.order import Order
from classes.discount import Discount

# Пример использования классов

# Создаем продукты
product1 = Product("Товар 1", 1000.0)
product2 = Product("Товар 2", 2000.0)
product3 = Product("Товар 3", 1500.0)

# Создаем клиентов и добавляем их в список
customers = []
customer1 = Customer("Иван")
customer2 = Customer("Анна")
customers.append(customer1)
customers.append(customer2)

# Создаем заказы
order1 = Order([product1, product2]) # Заказ клиента 1
order2 = Order([product3]) # Заказ клиента 2
order3 = Order([product1, product3]) # Заказ клиента 1

# Добавляем заказы к клиентам
customer1.add_order(order1)
customer1.add_order(order3)
customer2.add_order(order2)

# Создаем различные скидки
discount_seasonal = Discount("Сезонная скидка", 10) # 10% скидка
discount_promocode = Discount("Скидка по промокоду", 15) # 15% скидка

# Подсчитываем общую сумму по заказам с применением скидки
total_after_discount1 = Discount.apply_discount(order1, discount_seasonal)
total_after_discount2 = Discount.apply_discount(order2, discount_promocode)
total_after_discount3 = Discount.apply_discount(order3, discount_seasonal)

# Вывод информации о клиентах и их заказах
for customer in customers:
    print(customer)

print(order1)
print(f"Общая цена заказа 1 с учетом скидки: {total_after_discount1}")
print(order2)
print(f"Общая цена заказа 2 с учетом скидки: {total_after_discount2}")

# Общее количество заказов
print(f"Общее количество заказов: {Order.total_orders()}")

# Общая сумма всех заказов всех клиентов
total_sum_all_orders = sum(order.total_price() for customer in customers for order in customer.orders)
print(f"Общая сумма всех заказов: {total_sum_all_orders}")