# Проект 1.

## **Установка:**

Версия python для данного проекта `^3.13`

1. Установите Poetry:
```
https://install.python-poetry.org | python -
```
2. Клонируйте репозиторий:
```
git clone https://github.com/KolDaria/Project_1
```
3. Установите зависимости:
```
poetry add requests
```

## **Использование:**

### *Проект содержит:*

#### Папку `src` в которой реализованны следующие функции:

1. `__init__`: инициализация объекта.
2. `Category`: создан класс по категории продуктов.
3. `Product`: создан класс для описания продукта.
4. `reading_json`: функция для чтения JSON-файла.
5. `objects_json`: функция для подгрузки данных по категориям и товарам из файла JSON.
6. `14.1_main.py`: модуль для проверки функциональностей между собой.

#### Папку `tests` в которой реализованно следующее:

1. `__init__`: инициализация объекта.
2. `test_utils.py`: модуль для тестирования функций `reading_json, objects_json`.
3. `test_category.py`: модуль для тестирования класса `Category`.
4. `test_product.py`: модуль для тестирования класса `Product`.

#### Папку `data` которая содержит:

1. `products.json`: файл содержащий категории и товары.

##### Примеры использования функций `reading_json, objects_json`:

```python
# Пример для функции reading_json

path_json = os.path.dirname(__file__)  # входной аргумент
<class 'list'>  # выход функции

# Пример для функции objects_json
<class 'list'>  # входной аргумент
category_data[0].name == "Смартфоны"
len(category_data[0].products) == 3  # выход функции
```

## Тестирование функций:

```
---------- coverage: platform win32, python 3.13.0-final-0 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
config.py                    4      0   100%
src\__init__.py              0      0   100%
src\category.py             28      0   100%
src\product.py              34      0   100%
src\utils.py                19      0   100%
tests\__init__.py            0      0   100%
tests\conftest.py           16      0   100%
tests\test_category.py      22      0   100%
tests\test_product.py       34      0   100%
tests\test_utils.py          6      0   100%
--------------------------------------------
TOTAL                      163      0   100%



```

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).