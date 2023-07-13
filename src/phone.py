from src.item import Item

class Phone(Item):
    """
    Класс для представления телефона в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название телефона.
        :param price: Цена за единицу телефона.
        :param quantity: Количество телефонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        if not number_of_sim > 0:
            raise ValueError
        self._number_of_sim = number_of_sim


    def __add__(self, other):
        """
        Позволяет складывать экземпляры класса Phone и Item зная количество товара в магазине.

        :param other: Другой экземпляр класса Phone или Item.
        :return: Экземпляр класса Phone или Item с обновленным количеством товара в магазине.
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать экземпляры классов Phone и Item с экземплярами других классов.")

    def __repr__(self):
        return f"Phone('{self._name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):
        return str(self._name)

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if (type(value) != int) or value < 0:
            raise ValueError
        else:
            self._number_of_sim = value