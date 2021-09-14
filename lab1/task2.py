import sys
import operator

try:
    math_function = getattr(operator, sys.argv[1])
    print(math_function(float(sys.argv[2]), float(sys.argv[3])))
except BaseException:
    print("Incorrect data\nNOTE! use only binary operations")