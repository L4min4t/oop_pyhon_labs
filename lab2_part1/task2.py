# Create a class called Rational for performing arithmetic with fractions.
# Write a program to test your class. Use integer variables to represent the private data of the class
# – the numerator and the denominator. Provide a __init__() method that enables an object of this class
# to be initialized when it’s declared. The __init__() should contain default parameter values in case no
# initializers are provided and should store the fraction in reduced form. For example, the fraction 2/4 would
# be stored in the object as 1 in the numerator and 2 in the denominator. Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format. (отредактировано) 

from math import gcd

class Rational:
    def __init__(self, num = 1, den = 1):
        if not(isinstance(num, int)) or not(isinstance(den, int)):
            raise TypeError('value must be int')
        if not den:
            raise ZeroDivisionError('denominator shouldn`t be zero')
        div = gcd(num, den)
        self.__numerator = num // div
        self.__denominator = den // div
    
    def fractional_form(self):
        return f"{self.__numerator}/{self.__denominator}"

    def float_form(self):
        return self.__numerator/self.__denominator
        
try:
    rat = Rational(2, 4)
    print(rat.float_form())
    print(rat.fractional_form())
except Exception as e:
    print(e)
