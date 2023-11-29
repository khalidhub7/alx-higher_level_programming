#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
mode = number % 10 if number > 10 else number % -10
if (mode) > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, mode, end = ""))
elif (mode) < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, mode, end = ""))
elif (mode) == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, mode, end = ""))
