from src.phone import Phone

p1 = Phone("iPhone 14", 120, 10, 2)

def test___str__():
    assert str(p1) == 'iPhone 14'

def test___repr__():
    assert repr(p1) == "Phone('iPhone 14', 120, 10, 2)"


