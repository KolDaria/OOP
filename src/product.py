from abc import ABC, abstractmethod
from typing import Any

from src.print_mixin import PrintMixin


class BaseProduct(ABC):
    """
    Абстрактный класс выводит общие свойства из класса «Продукты»
    """

    @classmethod
    @abstractmethod
    def new_product(cls: Any, *args: Any, **kwargs: Any) -> Any:
        pass


class Product(BaseProduct, PrintMixin):
    """
    Класс для описания продукта
    """
    products: list = []
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
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self: Any) -> str:
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self: Any, other: Any) -> Any:
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, data: dict) -> Any:
        for product in cls.products:
            if product.name == data["name"]:
                product.quantity += data["quantity"]
                product.price = max(product.price, data["price"])
                return product
        new_product = cls(**data)
        cls.products.append(new_product)
        return new_product

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: int) -> Any:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > new_price:
                user_input = input("Подтверждаете понижение цены yes(y)/no(n): ")
                if user_input.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price


class Smartphone(Product):
    """
    Дочерний класс описания продукта (смартфон)
    """
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self: Any, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str) -> None:
        """
        Метод переопределения базового класса
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Дочерний класс описания продукта (трава газонная)
    """
    country: str
    germination_period: str
    color: str

    def __init__(self: Any, name: str, description: str, price: float, quantity: int, country: str,
                 germination_period: str, color: str) -> None:
        """
        Метод переопределения базового класса
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
