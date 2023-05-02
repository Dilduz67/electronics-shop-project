import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    inst_from_csv = 0
    csv_file_name:str = None
    @classmethod
    def instantiate_from_csv(cls, csv_name='') -> None:
        #global csv_file_name
        cls.all.clear()
        Item.inst_from_csv=1
        if csv_name=='':
            cls.csv_file_name='..\\src\\items.csv'
        else:
            cls.csv_file_name=csv_name

        try:
            with open(cls.csv_file_name) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_class = Item(row['name'], row['price'], row['quantity'])
                    cls.all.append(new_class)
        except FileNotFoundError:
            print("Отсутствует файл items.csv.")
        except KeyError as k:
            raise InstantiateCSVError from None

        Item.inst_from_csv = 0

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()  # Вызов конструктора родительского класса

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

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден.'

    def __str__(self):
        return self.message