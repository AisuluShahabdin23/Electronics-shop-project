from src.item import Item


class MixinLanguage:
    """
    Миксин для изменения языка (раскладки клавиатуры)
    """
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Изменяет язык клавиатуры
        """
        if self.language == 'EN':
            self.__language = 'RU'
            return self
        elif self.language == 'RU':
            self.__language = 'EN'
            return self


class Keyboard(Item, MixinLanguage):
    """
    Класс для товара “клавиатура”
    """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
