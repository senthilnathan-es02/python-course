# Write a Python program to check if a given year is a leap year or not.

# Instructions:
# A year is a leap year if:
# It is divisible by 4 and not divisible by 100, or
# It is divisible by 400.
# Take the year as input from the user.
# Use the above rules to determine if it's a leap year.

year = int (input())
if (year%4==0 and year%100!=0) or (year%400==0) :
    print("This year is leap year")
else:
    print("Not leap year ")
