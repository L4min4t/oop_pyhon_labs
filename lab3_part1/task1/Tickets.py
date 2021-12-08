from datetime import datetime
import random

ADVANCE_DISCOUNT = 0.6
STUDENT_DISCOUNT = 0.5
LATE_DISCOUNT = 1.1

class Regular_ticket:
    def __init__(self, event_name, date, price, id=0):
        self.event_name = event_name
        self.date = date
        self.price = price
        self.id = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('id must be int')
        if value == 0:
            self.__id = int(hash(str(random.random()) + str(datetime.now())))
        else:
            self.__id = value


    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        if not isinstance(value, str):
            raise TypeError('event name must be a string')
        if not value.strip():
            raise ValueError('event name is empty')
        self.__event_name = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('date must be a string')
        if not value.strip():
            raise ValueError('date is empty')
        try:
            date_time_obj = datetime.strptime(value, '%d-%m-%y')
        except ValueError:
            raise ValueError('invalid date')
        self.__date = date_time_obj

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('price must be a float')
        if value <= 0:
            raise ValueError('the price must be greater than zero')
        self.__price = value

    def to_dict(self):
        dump = {}
        prop = {}
        prop['type'] = self.__class__.__name__
        prop['event_name'] = self.__event_name
        prop['date'] = self.__date.strftime('%d-%m-%y')
        prop['price'] = self.__price
        dump[f'{self.__id}'] = prop
        return dump

    @staticmethod
    def from_dict(dump):
        for item in dump.keys():
                return Regular_ticket(dump[item]['event_name'], dump[item]['date'], dump[item]['price'], item)


    def __str__(self):
        return f'\t\tTICKET ID: {self.id}\nType: {self.__class__.__name__}\nEvent name: {self.event_name}\nDate: {self.__date.date()}\nPrice: {self.__price}'


class Advance_ticket(Regular_ticket):
    def __init__(self, event_name, date, price, id=0):
        super(Advance_ticket, self).__init__(event_name, date, price * ADVANCE_DISCOUNT, id)
    @staticmethod
    def from_dict(dump):
        for item in dump.keys():
            return Advance_ticket(dump[item]['event_name'], dump[item]['date'], dump[item]['price'], item)



class Late_ticket(Regular_ticket):
    def __init__(self, event_name, date, price, id=0):
        super(Late_ticket, self).__init__(event_name, date, price * LATE_DISCOUNT, id)

    @staticmethod
    def from_dict(dump):
        for item in dump.keys():
            return Late_ticket(dump[item]['event_name'], dump[item]['date'], dump[item]['price'], item)



class Student_ticket(Regular_ticket):
    def __init__(self, event_name, date, price, id=0):
        super(Student_ticket, self).__init__(event_name, date, price * STUDENT_DISCOUNT, id)

    @staticmethod
    def from_dict(dump):
        for item in dump.keys():
            return Student_ticket(dump[item]['event_name'], dump[item]['date'], dump[item]['price'], item)
