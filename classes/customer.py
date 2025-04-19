class Customer:
    """Класс Customer

Этот класс представляет клиента интернет-магазина.

Атрибуты:
name (str): Имя клиента.
orders (list): Список заказов клиента.

Метод __init__:
Конструктор принимает имя клиента и инициализирует список заказов.
Пример: customer1 = Customer("Иван").

Метод add_order:
Добавляет заказ в список заказов клиента.
Аргументы:
order (Order): Заказ для добавления.

Метод __str__:
Возвращает строковое представление объекта клиента, включая количество заказов.
Пример: print(customer1) выведет "Клиент(name: Иван, orders_count: 0)".

Метод __repr__:
Возвращает представление объекта клиента в формате для разработчика.
Пример: repr(customer1) вернет "Customer(name=Иван)".
"""

    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Клиент(name: {self.name}, orders_count: {len(self.orders)})"

    def __repr__(self):
        return f"Customer(name={self.name})"