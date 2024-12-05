# Write a Python program to check if a number is prime or not.

# A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
# For example:

# 2, 3, 5, 7, and 11 are prime numbers.
# 4, 6, 8, 9, and 12 are not prime numbers.
import math


user = int(input())
isprime = True

if user<=1:
        isprime =  False
    
else:
    for i in range(2, int(math.sqrt(user))+1):
        if user%i==0:
            isprime = False
        break

if isprime:
    print ("this is prime")
else:
    print("this is not prime number")
