#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = (-1) * (abs(number) % 10)
else:
    last_number = number % 10
print(f"Last digit of {number} is {last_number} and is", end=" ")
if last_number > 5:
    print("greater than 5")
elif last_number == 0:
    print("0")
elif (last_number < 6) and (last_number != 0):
    print("less than 6 and not 0")
