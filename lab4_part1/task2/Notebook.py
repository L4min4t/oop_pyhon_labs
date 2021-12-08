from Person import Person

class Notebook:
    def __init__(self, *args):
        self.records = list(args)

    @property
    def records(self):
        return self.__records

    @records.setter
    def records(self, val):
        if not all(isinstance(x, Person) for x in val):
            raise TypeError('person must be Person type')
        self.__records = val

    def __add__(self, other):
        if not isinstance(other, Person):
            raise TypeError('person must be Person type')
        self.__records.append(other)
        return self
        # container = self.__records
        # container.append(other)
        # return Notebook(*container)

    def __sub__(self, other):
        if not isinstance(other, Person):
            raise TypeError('person must be Person type')
        self.__records.remove(other)
        return self
        # container = self.__records
        # container.remove(other)
        # return Notebook(*container)

    def __mul__(self, val):
        if not isinstance(val, str):
            raise TypeError('searching field must be str')
        for rec in self.__records:
            if rec.name == val or rec.surname == val or rec.phone == val or rec.birthday == val:
                return rec

    def __str__(self):
        return '\n'.join([str(x) for x in self.__records])