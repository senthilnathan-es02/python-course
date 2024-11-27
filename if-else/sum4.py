# Write a Python program that takes three numbers as input from the user and determines the largest among them.

# Instructions:
# Ask the user to enter three numbers.
# Use if-elif-else statements to find the largest number.
# Print the largest number.

num1 = input()
num2 = input()
num3 = input()

if num1 > num2 and num1 > num3:
    largest = num1

elif num2>num1 and num2>num3:
    largest = num2

else:
    largest = num3

    print("Largest number is",largest)

