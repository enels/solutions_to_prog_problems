class Flower:

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_petals(self, total):
        self._petals = total

    def get_petals(self):
        return self._petals

    def set_price(self, amount):
        self._price = amount