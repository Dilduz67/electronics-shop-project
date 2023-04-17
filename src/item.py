import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    inst_from_csv = 0
    @classmethod
    def instantiate_from_csv(cls) -> None:
        cls.all.clear()
        Item.inst_from_csv=1
        with open('..\\src\\items.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_class = Item(row['name'], row['price'], row['quantity'])
                cls.all.append(new_class)

        Item.inst_from_csv = 0


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        if Item.inst_from_csv == 0:
            self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        try:
            assert len(name) <= 10
        except AssertionError:
            print("Длина наименования товара не больше 10 симвовов!")
        else:
            self.__name = name

    @staticmethod
    def string_to_number(num_str):
        val=0
        try:
            val = int(float(num_str))
        except ValueError:
            print("Передано неверное значение!")

        return val

    #магические методы
    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name