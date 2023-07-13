import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    """
    Создание экземпляра класса Phone для тестирования.
    """
    return Phone("Phone 1", 100.0, 5, 2)

def test_phone_initialization(phone):
    """
    Тестирование инициализации экземпляра класса Phone.
    """
    assert phone.name == "Phone 1"
    assert phone.price == 100.0
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_phone_addition_with_phone(phone):
    """
    Тестирование сложения экземпляров класса Phone.
    """
    other_phone = Phone("Phone 2", 150.0, 3, 1)
    result = phone + other_phone
    assert result == 8  # Общее количество телефонов (5 + 3)

def test_phone_addition_with_item(phone):
    """
    Тестирование сложения экземпляра класса Phone и экземпляра класса Item.
    """
    item = Item("Item 1", 10.0, 2)
    result = phone + item
    assert result == 7  # Общее количество товара в магазине (5 + 2)

def test_phone_addition_with_another_class(phone):
    """
    Тестирование сложения экземпляра класса Phone с экземпляром другого класса.
    """
    with pytest.raises(TypeError):
        result = phone + "some_object"
