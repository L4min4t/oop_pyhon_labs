# 1. Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;+
# - subtracting two Rational numbers. The result should be stored in reduced form;+
# - multiplying two Rational numbers. The result should be stored in reduced form;+
# - dividing two Rational numbers. The result should be stored in reduced form;+
# - comparison two Rational numbers.

from Rational import Rational

def main():
    x = Rational(3, 7)
    x1 = Rational(3, 7)
    print(x <= x1)

if __name__ == "__main__":
    main()