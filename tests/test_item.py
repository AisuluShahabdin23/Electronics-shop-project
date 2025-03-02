"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

Item.pay_rate = 0.8


def test_calculate_total_price():
    total1 = item1.calculate_total_price()
    assert total1 == 200000
    total2 = item2.calculate_total_price()
    assert total2 == 100000


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv('src/test2.csv') == 'Отсутствует файл src/test2.csv'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'