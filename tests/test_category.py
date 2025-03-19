from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_init_category(first_category: Any, second_category: Any) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, но и "
                                          "получения дополнительных функций для удобства жизни")
    assert len(first_category.in_products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products(first_category: Any) -> Any:
    assert first_category.productss == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")


def test_category_add_product(first_category: Any, product: Any) -> Any:
    first_category.add_product(product)
    assert len(first_category.in_products) == 4


def test_add_non_product() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1]
    )
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_category_str(first_category: Any) -> Any:
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator: Any) -> Any:
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == '55" QLED 4K'

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_init_category_products(first_category: Any, second_category: Any) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, но и "
                                          "получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3
