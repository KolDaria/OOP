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


def test_product_price_setter() -> Any:
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 100, 5)
    new_product.price = 1000
    assert new_product.price == 1000


def test_product_price_setter_decrease(capsys: Any) -> Any:
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 2000, 5)
    with patch('builtins.input', return_value='y') as mock_input:
        new_product.price = 1000
        mock_input.assert_called_once_with("Подтверждаете понижение цены yes(y)/no(n): ")
        assert new_product.price == 1000


def test_new_product_existing_product() -> Any:
    Product.products = [Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера",
                                price=180000.0, quantity=5)]
    data = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "quantity": 20,
            "price": 190000.0}
    result = Product.new_product(data)
    assert result.quantity == 25
    assert result.price == 190000.0
