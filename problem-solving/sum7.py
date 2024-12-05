# Write a Python program to find the factorial of a given number.
user = int(input())
fact = 1
for i in range(1,user+1):
    fact*=i
print(fact)