from src.item import Item

# 5 ////////

class KeyboardLayoutMixin:
    def change_lang(self, new_lang=None):
        if new_lang is not None:
            if new_lang not in ['EN', 'RU']:
                raise ValueError("Unsupported language")
            self.language = new_lang
        else:
            if self.language == "EN":
                self.language = "RU"
            elif self.language == "RU":
                self.language = "EN"
        return self


class Keyboard(Item, KeyboardLayoutMixin):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        if language not in ['EN', 'RU']:
            raise AttributeError
        self.language = language


