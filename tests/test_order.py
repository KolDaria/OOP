from typing import Any

import pytest

from src.category import Category
from src.order import Order
from src.product import Product


def test_order_info() -> Any:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5)
    order = Order("Тестовый заказ", "Описание заказа", product, 2)
    assert order.get_info() == ("Заказ: Тестовый заказ, товар: Samsung Galaxy S23 Ultra, количество: 2, "
                                "итоговая стоимость: 360000.0")


def test_category_info() -> Any:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                        "функций для удобства жизни", [product1, product2])
    total_quantity = product1.quantity + product2.quantity
    assert category.get_info() == f"Категория: Смартфоны, количество продуктов: {total_quantity} шт."


@pytest.mark.parametrize("name, description, expected_str", [
    ("Смартфоны", "Смартфоны, как средство..", "Смартфоны: Смартфоны, как средство.."),
    ("Телевизоры", "Современный телевизор, который..", "Телевизоры: Современный телевизор, который.."),
])
def test_entity_str(name: str, description: str, expected_str: str) -> Any:
    entity = Order(name, description, Product("Samsung Galaxy S23 Ultra",
                                              "256GB, Серый цвет, 200MP камера", 180000.0, 5), 0)
    assert str(entity) == expected_str
