# Визначити клас ЦИФРОВИЙ ЛІЧИЛЬНИК.
# Лічильник - це змінна з обмеженим діапазоном, який скидається у початковий стан,
# коли її цілочисельне значення досягає визначеного максимуму.

# Визначити методи встановлення і виведення значень полів даних.
# Забезпечити можливість встановлення максимального і мінімального значень, зчитування поточного значення.

# Перевантажити операцію += для збільшення значення лічильника, -= для зменшення значення лічильника.

# Визначити похідний клас СЕКУНДОМІР з додатковими полями даних, які позначають включення та виключення секундоміра.
# Визначити операторні методи зчитування та виведення значення заміряного часу.

# Розробити клас РЕЗУЛЬТАТИ спринтерського забігу, який містить послідовність об'єктів класу СЕКУНДОМІР.
# Визначити найменший та найбільший час забігу, середнє значення часу забігу, результати часу для трьох переможців змагання.

# Для роботи із послідовністю об'єктів побудувати та використати клас-ітератор.


from datetime import datetime
from time import sleep


class Counter:
    def __init__(self, val=0, max=250, min=0):
        if max <= min:
            raise ValueError('no logic in min-max')
        self.max = max
        self.min = min
        self.value = val
        pass

    @property
    def max(self):
        return self.__max

    @property
    def min(self):
        return self.__min

    @property
    def value(self):
        return self.__value

    @max.setter
    def max(self, val):
        if not isinstance(val, int):
            raise TypeError('counter must be int')
        self.__max = val

    @min.setter
    def min(self, val):
        if not isinstance(val, int):
            raise TypeError('counter must be int')
        self.__min = val

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise TypeError('counter must be int')
        if val > self.max:
            self.__value = self.min
            raise ValueError('reached the maximum, counter was reset to its min value')
        self.__value = val

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError('counter must be int')
        if self.__value + other > self.max:
            self.__value = self.min
            print('reached the maximum, counter was reset to its min value')
            # raise ValueError('reached the maximum, counter was reset to its original value')
            return self
        self.__value += other
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError('counter must be int')
        if self.__value - other < self.min:
            self.__value = self.min
            print('reached the minimum')
            # raise ValueError('reached the minimum')
            return self
        self.__value -= other
        return self


class Timer(Counter):
    __time_of_start = None
    __time_of_end = None
    def __init__(self, val=0, max=250, min=0, is_on=False):
        Counter.__init__(self, val, max, min)
        self.is_on = is_on

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, val):
        if not isinstance(val, bool):
            raise TypeError('is_on must be bool')
        self.__is_on = val

    def start(self):
        self.is_on = True
        while True:
            self.value = self.value + 1
            sleep(1)
            print(self.value)
            if input('continue - enter, to stop eny input here'):
                break
                # тут треба уміти працювати з потоками, щоб зробити нормальний таймер, а я ще не працював з ними




def main():
    x = Timer(5, 2000, 3)
    x.start()

if __name__ == "__main__":
    main()
