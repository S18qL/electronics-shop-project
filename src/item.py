import csv
# from src.phone import Phone

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Getter для получения названия товара.

        :return: Название товара.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter для задания названия товара.

        :param value: Название товара.
        """
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        # cls.all = []
        try:
            with open('src/items.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        item = cls(row['name'], float(row['price']), int(row['quantity']))
                        if item not in cls.all:
                            cls.all.append(item)
                    except Exception:
                        raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует числовую строку в число.

        :param value: Числовая строка.
        :return: Число.
        """

        return int(float(value))

    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self._name)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать экземпляры классов Phone и Item с экземплярами других классов.")


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'InstantiateCSVError, {0} '.format(self.message)
        else:
            return 'InstantiateCSVError has been raised'
