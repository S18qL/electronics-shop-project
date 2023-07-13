"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
import csv
from src.item import Item


@pytest.fixture
def item():
    return Item("Test Item", 10.0, 5)


def test_item_initialization(item):
    assert item.name == "Test Item"
    assert item.price == 10.0
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    assert item.price == 10.0

    item.apply_discount()
    assert item.price == 10.0  # Скидка не применяется, self.pay_rate равно 1.0

    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0  # Скидка применена: 10.0 * 0.8 = 8.0


def test_modify_class_variable():
    item1 = Item("Item 1", 10.0, 5)
    item2 = Item("Item 2", 15.0, 3)
    item3 = Item("Item 3", 20.0, 2)

    assert Item.all == [item1, item2, item3]


def test_modify_instance_variable(item):
    assert item.quantity == 5

    item.quantity = 10
    assert item.calculate_total_price() == 100.0

# 2 ///////////

def test_instantiate_from_csv():
    # Проверяем, что экземпляры создаются из CSV-файла
    Item.all = []
    Item.instantiate_from_csv()

    # Проверяем, что количество созданных экземпляров верно
    for i in Item.all:
        print(i.name, i.price, i.quantity)
    assert len(Item.all) == 5

    # Проверяем значения для каждого созданного экземпляра
    assert Item.all[0].name == 'Lenovo'
    assert Item.all[0].price == 100.0
    assert Item.all[0].quantity == 1

    assert Item.all[1].name == 'Apple'
    assert Item.all[1].price == 1000.0
    assert Item.all[1].quantity == 3

    assert Item.all[2].name == 'Xiaomi'
    assert Item.all[2].price == 10.0
    assert Item.all[2].quantity == 5


def test_string_to_number():
    # Проверяем преобразование числовой строки в число
    assert Item.string_to_number('10.5') == 10
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('20.0') == 20
    assert Item.string_to_number('25.89') == 25

    # Проверяем, что тип возвращаемого значения - int
    assert isinstance(Item.string_to_number('15'), int)




# 3 //////////////


def test_item_repr():
    item = Item("Apple", 2.5, 10)
    assert repr(item) == "Item('Apple', 2.5, 10)"

def test_item_str():
    item = Item("Banana", 1.5, 5)
    assert str(item) == "Banana"



# 4 ///////
from src.phone import Phone

@pytest.fixture
def phone():
    """
    Создание экземпляра класса Phone для тестирования.
    """
    return Phone("Phone 1", 100.0, 5, 2)

def test_phone_addition_with_item(phone):
    """
    Тестирование сложения экземпляра класса Phone и экземпляра класса Item.
    """
    item = Item("Item 1", 10.0, 2)
    result = phone + item
    assert result == 7  # Общее количество товара в магазине (5 + 2)



# 6 ///////

from src.item import InstantiateCSVError

def test_instantiate_from_csv_1():
    # Тест с имеющимся файлом
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_instantiate_from_csv_file_not_found():
    # Тест проходит, если указан неверный путь к файлу
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

def test_instantiate_from_csv_corrupted_file():
    # Тест для поврежденного файла
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()



if __name__ == "__main__":
    pytest.main()
