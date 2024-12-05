# Write a Python program to check if a given number is a perfect number.

# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
# For example, 6 is a perfect number because its divisors are 1, 2, and 3, and 
# 1
# +
# 2
# +
# 3
# =
# 6
# 1+2+3=6.

user = int(input())
for i in range(user):
    if i%1==0 and i%2==0 and i%3==0:
        print("Perfect Number")
        break

    else:
        print("Not perfect number")


