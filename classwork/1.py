import os
import random
import timeit

# x = open("1.txt", "w+")
# x.truncate()
# while os.path.getsize("1.txt") < 52428800:
#     x.write(str(random.randrange(1000)) + "\n")


s = """
sum = 0
x = open("1.txt", "r")
for line in x:
    if line.strip().isdigit():
        sum += int(line)
x.close()
"""

print(timeit.timeit(s, number = 1))

s = """
sum = 0
x = open("1.txt", "r")
lines = x.readlines()
for line in lines:
    if line.strip().isdigit():
        sum += int(line)
x.close()
"""

print(timeit.timeit(s, number = 1))

s = """
file = open("1.txt", "r")
nums = (int(line.strip()) for line in file if line.strip().isdigit())
sum1 = sum(nums)
file.close()
"""

print(timeit.timeit(s, number = 1))