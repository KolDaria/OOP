from typing import Any


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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
