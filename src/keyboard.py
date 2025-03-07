from src.item import Item

class MixinChangeLang:
    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        if self._language=="EN":
            self._language= "RU"
        else:
            self._language= "EN"

        return (self)

class Keyboard(Item,MixinChangeLang):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

        self._language="EN"
    @property
    def language(self):
        return self._language

