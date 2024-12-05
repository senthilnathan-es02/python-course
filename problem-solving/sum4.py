# Prime Number Checker
# Write a program to check if a number is a prime number.
# Example:
# Input: 29
# Output: True

import math


user = int(input("Enter a number: "))
isprime = True
if user <= 1:
    isprime = False
else:
    for i in range(2, int(math.sqrt(user)) + 1):
        if user % i == 0:
            isprime = False
            break


if isprime:
    print(f"{user} is a prime number.")
else:
    print(f"{user} is not a prime number.")
