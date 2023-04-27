from src.keyboard import Keyboard


k = Keyboard("KB1", 10, 10)

def test___str__():
    assert str(k) == 'KB1'

