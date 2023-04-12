from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
