#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_num = number % 10
if number < 0:
    last_num = number % -10
if last_num > 5:
    str = ("and is greater than 5")
elif (last_num) < 6 and (last_num) != 0:
    str = ("and is less than 6 and not 0")
else:
    str = ("and is 0")
print(f"Last digit of {number} is {last_num} {str}")
