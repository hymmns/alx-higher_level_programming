#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of {:d} is ".format(number), end="")
if number > 5:
    print("{:d} and is greater than 5".format(last_digit))
elif number == 0:
    print("{:d} and is 0".format(last_digit))
else:
    print("-{:d} and is less than 6 and not 0".format(last_digit))
