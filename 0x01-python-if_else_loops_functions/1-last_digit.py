#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num_str = str(number)
last_num = int(num_str[-1])
if number < 0:
    last_num = last_num*-1
if last_num > 5:
    str = ("and is greater than 5")
elif (last_num) < 6 and (last_num) != 0:
    str = ("and is less than 6 and not 0")
else:
    str = ("and is 0")
print(f"Last digit of {number} is {last_num} {str}")
