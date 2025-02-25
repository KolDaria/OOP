from typing import Any


class Product:
    """
    Класс для описания продукта
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self: Any, name: str, description: str, price: float, quantity: int) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
