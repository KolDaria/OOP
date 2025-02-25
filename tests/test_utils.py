from src.utils import objects_json, path_json, reading_json


def test_objects_json() -> None:
    data_r = reading_json(path_json)
    category_data = objects_json(data_r)

    assert category_data[0].name == "Смартфоны"
    assert len(category_data[0].products) == 3
