# the name, surname, number phone and birthday of person
import re

class Person:
    def __init__(self, name, surname, phone, birthday):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    @property
    def birthday(self):
        return self.__birthday

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('name must be a string')
        if not val.strip():
            raise ValueError('name is empty')
        self.__name = val.strip()

    @surname.setter
    def surname(self, val):
        if not isinstance(val, str):
            raise TypeError('surname must be a string')
        if not val.strip():
            raise ValueError('surname is empty')
        self.__surname = val.strip()

    @phone.setter
    def phone(self, val):
        if not isinstance(val, str):
            raise TypeError('phone must be a string')
        if not val.strip():
            raise ValueError('phone is empty')
        if not re.fullmatch(r'^((\+380)(\d{9}))$', val):
            raise ValueError('invalid number')
        self.__phone = val

    @birthday.setter
    def birthday(self, val):
        if not isinstance(val, str):
            raise TypeError('birthday must be a string')
        if not val.strip():
            raise ValueError('birthday is empty')
        if not re.fullmatch(r'^(((0)([1-9])|(1)(\d)|(2)(\d)|(3)((0)|(1))).((0)([1-9])|(1)([1-2])).((19)|(20))(\d{2}))$', val):
            raise ValueError('invalid date of birth')
        self.__birthday = val

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__phone} {self.__birthday}'
