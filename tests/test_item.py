"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

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
