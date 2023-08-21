import csv
import math


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # return name
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls, file_path: str = '../src/items.csv'):
        try:
            Item.all.clear()
            with open(file_path) as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    name, price, quantity = row
                    if price.isalpha():
                        continue
                    Item.all.append(cls(name, price, quantity))
                    # print(len(Item.all))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {file_path}')
        except Exception:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(str_num):
        return math.floor(float(str_num))

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
        self.price = self.price * Item.pay_rate
