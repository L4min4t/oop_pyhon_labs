import phonenumbers

class Customer:
    """
    holds customer info
    """
    id_generator = 0
    def __init__(self, surname, name, patronymic, mobile_phone):
        __slots__ = ['surname', 'name', 'patronymic', 'mobile_phone']
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone
        self.id = Customer.id_generator
        Customer.id_generator += 1

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value < Customer.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("surname must be string")
        if not surname.isalpha():
            raise ValueError("invalid surname")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be string")
        if not name.isalpha():
            raise ValueError("invalid name")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("patronymic must be string")
        if not patronymic.isalpha():
            raise ValueError("invalid patronymic")
        self.__patronymic = patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone
        
    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not phonenumbers.is_possible_number(phonenumbers.parse(mobile_phone)):
            raise ValueError("uncorrect number")
        self.__mobile_phone = mobile_phone

    def __str__(self) -> str:
        return f'ID customer: {self.id}\n{self.surname}\n{self.name}\n{self.patronymic}\n{self.mobile_phone}'