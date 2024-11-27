# Question: Odd or Even Number Checker
# Write a Python program to check whether a number entered by the user is odd or even.

# Instructions:
# Take a number as input from the user.
# Use the modulo operator (%) to determine if the number is divisible by 2.
# If the number is divisible by 2 (remainder is 0), print "The number is even."
# Otherwise, print "The number is odd."

num = int(input())
if num %2==0:
    print ("this is even number ")
else:
    print ("this is odd number")

