from typing import Any
from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone


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
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


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


def test_product_str(product: Any) -> Any:
    assert str(product) == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_product_add() -> Any:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 180000.0 * 5 + 210000.0 * 8


def test_product_add_typeerror() -> Any:
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_product_smartphone_init(product_smartphone1: Any) -> Any:
    assert product_smartphone1.name == "Iphone 15"
    assert product_smartphone1.description == "512GB, Gray space"
    assert product_smartphone1.price == 210000.0
    assert product_smartphone1.quantity == 8
    assert product_smartphone1.efficiency == 98.2
    assert product_smartphone1.model == "15"
    assert product_smartphone1.memory == 512
    assert product_smartphone1.color == "Gray space"


def test_product_lawngrass_init(product_lawngrass1: Any) -> Any:
    assert product_lawngrass1.name == "Газонная трава"
    assert product_lawngrass1.description == "Элитная трава для газона"
    assert product_lawngrass1.price == 500.0
    assert product_lawngrass1.quantity == 20
    assert product_lawngrass1.country == "Россия"
    assert product_lawngrass1.germination_period == "7 дней"
    assert product_lawngrass1.color == "Зеленый"


def test_print_mixin(capsys: Any) -> Any:
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
