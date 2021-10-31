#  Створити клас ЧАСУ з полями у закритій частині: година (0-23), хвилини (0-59), секунди (0-59).
#  Клас має конструктор, методи встановлення часу, методи отримання години, хвилини і секунди,
#  а також два методи виведення за шаблонами: "16 годин 18 хвилин 3 секунди" і "4 p.m. 18 хвилин З секунди".
#  Методи встановлення полів класу повинні перевіряти коректність параметрів, що задаються.

class My_clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if not isinstance(value, int):
            raise TypeError('hours must be int')
        if value < 0 or value > 23:
            raise ValueError('hours must be in range 0 - 23')
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if not isinstance(value, int):
            raise TypeError('minutes must be int')
        if value < 0 or value > 59:
            raise ValueError('minutes must be in range 0 - 59')
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if not isinstance(value, int):
            raise TypeError('seconds must be int')
        if value < 0 or value > 59:
            raise ValueError('seconds must be in range 0 - 59')
        self.__seconds = value

    def set_new_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def twelve_hour_format(self):
        temp = ''
        if self.hours > 12:
            temp = f'{self.hours - 12} p.m.'
        else:
            temp = f'{self.hours} a.m.'
        return f'{temp} {self.minutes} хвилин {self.seconds} секунд'
    
    def full_hour_format(self):
        return f'{self.hours} годин {self.minutes} хвилин {self.seconds} секунд'
    
    def __str__(self) -> str:
        return f'{self.hours} годин {self.minutes} хвилин {self.seconds} секунд'

try:
    clock = My_clock(16, 25, 59)
    print(clock)
    print(clock.twelve_hour_format())
    print(clock.full_hour_format())
    clock.set_new_time(12, 59, 59)
    print(clock)
    print(clock.hours)
    print(clock.twelve_hour_format())
    print(clock.full_hour_format())
except (TypeError, ValueError) as err:
    print(err)
