from datetime import datetime
from Tickets import *
import json
from dateutil.relativedelta import *
import os


class Event:
    def __init__(self, date, name, total_tickets, current_tickets, regular_ticket_price, tickets=[]):
        self.date = date
        self.name = name
        self.total_tickets = total_tickets
        self.current_tickets = current_tickets
        self.regular_ticket_price = regular_ticket_price
        self.tickets = tickets

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
        if date_time_obj <= datetime.now():
            raise ValueError('event ended')
        self.__date = date_time_obj

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        if not value.strip():
            raise ValueError('name is empty')
        self.__name = value.strip()

    @property
    def total_tickets(self):
        return self.__total_tickets

    @total_tickets.setter
    def total_tickets(self, value):
        if not isinstance(value, int):
            raise TypeError('total_tickets must be a int')
        if value <= 0:
            raise ValueError('no tickets - no event')
        self.__total_tickets = value

    @property
    def current_tickets(self):
        return self.__current_tickets

    @current_tickets.setter
    def current_tickets(self, value):
        if not isinstance(value, int):
            raise TypeError('current_tickets must be a int')
        if value < 0:
            raise ValueError('the number of tickets cannot be less than zero')
        self.__current_tickets = value

    @property
    def regular_ticket_price(self):
        return self.__regular_ticket_price

    @regular_ticket_price.setter
    def regular_ticket_price(self, value):
        if not isinstance(value, float):
            raise TypeError('regular ticket price must be a float')
        if value <= 0:
            raise ValueError('the price must be greater than zero')
        self.__regular_ticket_price = value

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, value):
        if not isinstance(value, list):
            raise TypeError('tickets must be a list')
        if not all(isinstance(el, Regular_ticket) for el in value):
            raise ValueError('tickets must consist of tickets')
        self.__tickets = value

    def __str__(self):
        result = f'\t\tEvent name: {self.__name}\nDate: {self.__date.date()}\nTotal tickets amount: {self.__total_tickets}\nCurrent tickets amount: {self.__current_tickets}\nRegular price: {self.__regular_ticket_price}\nPurchased tickets:\n'
        for ticket in self.__tickets:
            result += str(ticket) + '\n'
        return result

    @staticmethod
    def get_event(name):
        if os.path.exists('Events.json'):
            with open('Events.json', 'r') as f:
                dump = json.load(f)
                if name.strip() in dump.keys():
                    tickets = []
                    for item in dump[name]['tickets']:
                        tickets.append(Regular_ticket.from_dict({item: dump[name]['tickets'][item]}))
                    return Event(dump[name]['date'], name, dump[name]['total_tickets'], dump[name]['current_tickets'],
                                 dump[name]['regular_ticket_price'], tickets)
                else:
                    raise ValueError('event doesnt exist')
        else:
            raise OSError('file doesnt exist')

    def to_dict(self):
        dump = {}
        dump['date'] = self.date.strftime('%d-%m-%y')
        dump['total_tickets'] = self.total_tickets
        dump['current_tickets'] = self.current_tickets
        dump['regular_ticket_price'] = self.regular_ticket_price
        tick = {}
        for item in self.__tickets:
            tick.update(item.to_dict())
        dump['tickets'] = tick
        return dump

    def put_event(self):
        if os.path.exists('Events.json'):
            with open('Events.json', 'r') as f:
                dump = json.load(f)
                if self.__name in dump:
                    raise ValueError('event already exists')
                dump.update({self.__name: self.to_dict()})
            with open('Events.json', 'w') as f:
                json.dump(dump, f)
        else:
            raise OSError('file doesnt exist')

    def buy_ticket(self, date=datetime.now(), student=False):
        if self.__current_tickets < self.__total_tickets:
            if isinstance(date, str):
                date = datetime.strptime(date, '%d-%m-%y')
            if student:
                self.__current_tickets += 1
                self.__tickets.append(
                    Student_ticket(self.name, self.date.strftime('%d-%m-%y'), self.regular_ticket_price))
            else:
                if date > self.date:
                    raise ValueError('you are trying to buy a ticket for a finished self')
                elif date >= self.date + relativedelta(days=-10):
                    self.__current_tickets += 1
                    self.__tickets.append(
                        Late_ticket(self.name, self.date.strftime('%d-%m-%y'), self.regular_ticket_price))
                elif date + relativedelta(days=+60) <= self.date:
                    self.__current_tickets += 1
                    self.__tickets.append(
                        Advance_ticket(self.name, self.date.strftime('%d-%m-%y'), self.regular_ticket_price))
                else:
                    self.__current_tickets += 1
                    self.__tickets.append(
                        Regular_ticket(self.name, self.date.strftime('%d-%m-%y'), self.regular_ticket_price))
        else:
            raise ValueError('all tickets buied')

    def remove_ticket(self, id):
        if not isinstance(id, int):
            raise ValueError('id must be int')
        index = -1
        for i in range(0, len(self.__tickets)):
            if self.__tickets[i].id == id:
                index = i
                break
        if index != -1:
            self.__tickets.pop(index)
        else:
            raise LookupError('ticket with this id doesnt exist')

    def get_ticket_price_by_id(self, id):
        if not isinstance(id, int):
            raise TypeError('id must be int')
        for item in list(self.__tickets):
            if id == item.id:
                return item.price
        else:
            raise ValueError('ticket with this id doesnt exist')
