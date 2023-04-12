"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

p = Item('test',10,10)

def test_calculate_total_price():
    assert p.calculate_total_price()==100

def test_apply_discount():
    p.pay_rate=0.85
    p.apply_discount()
    assert p.price==8.5

def test_string_to_number():
    assert p.string_to_number('10') == 10

def tast_instantiate_from_csv():
    p.instantiate_from_csv()
    assert len(p.all) == 5



