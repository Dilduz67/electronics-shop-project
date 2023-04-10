"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

p = Item('test',10,10)

def test_calculate_total_price():
    assert p.total_price()==100

def test_apply_discount():
    assert p.discount_price()==85.0

