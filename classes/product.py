class Product:
    """Класс Product

Этот класс представляет товар в интернет-магазине.

Атрибуты:
name (str): Название товара.
price (float): Цена товара.

Метод __init__:
Конструктор принимает название и цену товара.
Пример: product1 = Product("Товар 1", 100.0).

Метод __str__:
Возвращает строковое представление объекта товара.
Пример: print(product1) выведет "Товар(name: Товар 1, price: 100.0)".

Метод __repr__:
Возвращает представление объекта товара в формате для разработчика.
Пример: repr(product1) вернет "Product(name=Товар 1, price=100.0)".

Метод __eq__:
Сравнивает два объекта товара по цене.
Пример: product1 == product2 проверит, равны ли товары по цене.

Метод __lt__:
Сравнивает два объекта товара по цене - возвращает True, если цена меньше.
Пример: product1 < product2 проверит, дешевле ли product1, чем product2.
"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар(name: {self.name}, price: {self.price})"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price