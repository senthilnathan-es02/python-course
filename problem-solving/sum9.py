# Write a Python program to find the Greatest Common Divisor (GCD) of two numbers.

# The GCD of two integers is the largest number that can divide both integers without leaving a remainder.
# For example:

# GCD of 12 and 15 is 3.
# GCD of 17 and 13 is 1 (since they are coprime).


user1 = int(input())
user2 = int(input())
gcd = min(user1,user2)
while gcd > 0:
    if user1%gcd==0 and user2%gcd==0:
        print(gcd)
        break
    gcd-=1
        
