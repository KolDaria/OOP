from typing import Any


class ProductIterator:
    def __init__(self: Any, category_obj: Any) -> None:
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self: Any) -> Any:
        return self

    def __next__(self: Any) -> Any:
        if self.index < len(self.category_obj.in_products):
            products = self.category_obj.in_products[self.index]
            self.index += 1
            return products
        else:
            raise StopIteration
