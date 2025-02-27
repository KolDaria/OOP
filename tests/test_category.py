from typing import Any


def test_init_category(first_category: Any, second_category: Any) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, но и "
                                          "получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4
