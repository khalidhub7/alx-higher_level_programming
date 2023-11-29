#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
mode = number % 10 if number > 10 else number % -10
print("Last digit of {} is {} and is ".format(number, mode), end = "")
if (mode) > 5:
    print("greater than 5")
elif (mode) < 6:
    print("less than 6 and not 0")
elif (mode) == 0:
    print("0")
