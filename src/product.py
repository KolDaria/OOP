from typing import Any


class Product:
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

    def __str__(self: Any) -> str:
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self: Any, other: Any) -> Any:
        return self.__price * self.quantity + other.__price * other.quantity

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
