# Write a Python program to check if a given string is a palindrome.

# A palindrome is a string that reads the same backward as forward.
# For example:

# "madam" is a palindrome.
# "hello" is not a palindrome.


user = input()

reverse = user[::-1]

if reverse == user :
    print("This is palindrome ")

else:
    print("This is not palinrome")
