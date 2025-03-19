from abc import ABC, abstractmethod

from src.product import Product


class OrderCategory(ABC):
    """
    Абстрактный класс выводит общие свойства из классов «Заказ» и «Категория»
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    @abstractmethod
    def get_info(self) -> str:
        pass


class Order(OrderCategory):
    """
    Выводит какой товар был куплен, количество купленного товара, а также итоговая стоимость.
    """

    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def get_info(self) -> str:
        return (f"Заказ: {self.name}, товар: {self.product.name}, количество: {self.quantity}, "
                f"итоговая стоимость: {self.total_cost}")
