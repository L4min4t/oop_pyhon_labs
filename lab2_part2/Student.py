from Record_book import Record_book

class Student:
    def __init__(self, name, surname, record_book):
        self.name = name
        self.surname = surname
        self.record_book = record_book

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be string')
        if name == '':
            raise ValueError('name mustn\'t be empty')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('surname must be string')
        if surname == '':
            raise ValueError('surname mustn\'t be empty')
        self.__surname = surname

    @property
    def record_book(self):
        return self.__record_book

    @record_book.setter
    def record_book(self, record_book):
        if not isinstance(record_book, Record_book):
            raise TypeError('record book must be Rcord_book')
        self.__record_book = record_book

    def __str__(self) -> str:
        return f'name: {self.name}\nsurname: {self.surname}\n{str(self.record_book)}'