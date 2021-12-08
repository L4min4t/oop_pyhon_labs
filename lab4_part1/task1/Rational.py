from math import gcd


class Rational:
    def __init__(self, num=1, den=1):
        self.numerator = num
        self.denominator = den
        self.reduce()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, val):
        if not isinstance(val, int):
            raise TypeError('numerator must be int')
        self.__numerator = val

    @denominator.setter
    def denominator(self, val):
        if not isinstance(val, int):
            raise TypeError('denominator must be int')
        if not val:
            raise ZeroDivisionError('denominator shouldn`t be zero')
        self.__denominator = val

    def reduce(self):
        div = gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // div
        self.__denominator = self.__denominator // div

    def float_form(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.__numerator+self.__denominator*other, self.__denominator)
        if isinstance(other, Rational):
            return Rational(self.__numerator*other.__denominator+other.__numerator*self.__denominator, self.__denominator*other.__denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            return Rational(self.__numerator-self.__denominator*other, self.__denominator)
        if isinstance(other, Rational):
            return Rational(self.__numerator*other.__denominator-other.__numerator*self.__denominator, self.__denominator*other.__denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.__numerator*other, self.__denominator)
        if isinstance(other, Rational):
            return Rational(self.__numerator*other.__numerator, self.__denominator*other.__denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.__numerator, self.__denominator*other)
        if isinstance(other, Rational):
            return Rational(self.__numerator*other.__denominator, self.__denominator*other.__numerator)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator+self.__denominator*other
            self.reduce()
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator*other.__denominator+other.__numerator*self.__denominator
            self.__denominator = self.__denominator*other.__denominator
            self.reduce()
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator - self.__denominator * other
            self.reduce()
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.reduce()
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator*other
            self.reduce()
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator*other.__numerator
            self.__denominator = self.__denominator*other.__denominator
            self.reduce()
            return self
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            self.__denominator = self.__denominator*other
            self.reduce()
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator*other.__denominator
            self.__denominator = self.__denominator*other.__numerator
            self.reduce()
            return self
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if self.__numerator == other.__numerator and self.__denominator == other.__denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        # return not self.__eq__(other)
        if not isinstance(other, Rational):
            return NotImplemented
        if self.__numerator != other.__numerator and self.__denominator != other.__denominator:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__numerator*other.__denominator > other.__numerator*self.__denominator:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__numerator*other.__denominator < other.__numerator*self.__denominator:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__numerator*other.__denominator >= other.__numerator*self.__denominator:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__numerator * other.__denominator <= other.__numerator * self.__denominator:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
