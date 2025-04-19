class Discount:
    """Класс Discount

Этот класс представляет систему скидок в интернет-магазине.

Атрибуты:
description (str): Описание скидки.
discount_percent (float): Процент скидки.

Метод __init__:
Конструктор принимает описание и процент скидки.
Пример: discount1 = Discount("Сезонная скидка", 10).

Метод apply_discount:
Применяет скидку к заказу.
Аргументы:
order (Order): Заказ, к которому применяется скидка.
discount (Discount): Скидка для применения.
Возвращает:
float: Общая стоимость заказа после применения скидки.
Пример: Discount.apply_discount(order1, discount1) вернет стоимость после применения скидки.

Метод __str__:
Возвращает строковое представление объекта скидки.
Пример: print(discount) выведет "Скидка(description: Сезонная скидка, percent: 10)".

Метод __repr__:
Возвращает представление объекта скидки в формате для разработчика.
Пример: repr(discount) вернет "Discount(description=Сезонная скидка, percent=10)".
"""

    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(order, discount):
        return order.total_price() * (1 - discount.discount_percent / 100)

    def __str__(self):
        return f"Скидка(description: {self.description}, percent: {self.discount_percent})"

    def __repr__(self):
        return f"Discount(description={self.description}, percent={self.discount_percent})"