from typing import Any
from unittest.mock import patch

from src.product import Product


def test_init_product(product: Any) -> Any:
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_new_product(new_product: Any) -> Any:
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_new_product_update(capsys: Any, product: Any) -> Any:
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


@patch('builtins.input', return_value='y')
def test_product_price_setter(mock_input: Any, capsys: Any, new_product: Any) -> Any:
    new_product.price = 1000
    message = capsys.readouterr()
    assert message.out.strip() == ''
    assert new_product.price == 1000
