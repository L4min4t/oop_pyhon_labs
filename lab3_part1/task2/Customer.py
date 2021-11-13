class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value != '':
            self.__name = value

    def __str__(self):
        return f'Customer:\n{self.name}\n'
