#!/usr/bin/python3
def fizzbuzz():
    numbers = range(1, 101)
    for i in numbers:
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(i), end=" ")
