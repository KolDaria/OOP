from typing import Any

from src.exceptions import ZeroQuantityError
from src.product import Product


class Category:
    """
    Класс по категории продуктов
    """
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self: Any, name: str, description: str, products: list | None = None) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self: Any) -> str:
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_info(self) -> str:
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"Категория: {self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Any) -> Any:
        """
        Метод для записи объекта класса Product в приватный атрибут списка товаров.
        """
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError("Количество товара не может равняться нулю")
            except ZeroQuantityError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError("Можно добавлять только экземпляры Product")

    @property
    def productss(self) -> Any:
        products_str = ""
        for products in self.__products:
            products_str += f'{str(products)}\n'
        return products_str

    @property
    def in_products(self) -> Any:
        return self.__products

    @property
    def products(self) -> Any:
        return self.__products

    def middle_price(self) -> Any:
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
