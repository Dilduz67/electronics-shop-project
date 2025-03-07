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

def test_instantiate_from_csv():
    p.csv_file_name='..\\src\\items.csv'
    p.instantiate_from_csv()
    if len(p.all) != 0:
        assert len(p.all) == 5

    p.csv_file_name = '..\\src\\bad_items.csv'
    Item.instantiate_from_csv()


def test___repr__():
    assert repr(p) == "Item('test', 8.5, 10)"

def test___str__():
    assert str(p) == 'test'

def test_instantiate_from_csv():
    Item.csv_file_name = '..\\src\\bad_items.csv'
    Item.instantiate_from_csv()

def test_instantiate_from_csv():
    Item.csv_file_name = '..\\src\\no_file.csv'
    Item.instantiate_from_csv()



