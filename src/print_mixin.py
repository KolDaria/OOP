class PrintMixin:
    """
    Класс-миксин, распечатывает в консоль информацию о том, от какого класса и с какими параметрами был создан объект
    """

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
