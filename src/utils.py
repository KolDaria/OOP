import json
from typing import Any

from config import PATH_JSON_FILE
from src.category import Category
from src.product import Product

path_json = PATH_JSON_FILE


def reading_json(path_json: str) -> Any:
    """
    Чтение JSON-файла
    """
    with open(path_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def objects_json(data: Any) -> list:
    """
    Подгрузка данных по категориям и товарам из файла JSON
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
