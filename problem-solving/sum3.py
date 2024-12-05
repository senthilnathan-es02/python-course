# FizzBuzz
# Print numbers from 1 to 100. For multiples of 3,
#  print "Fizz"; for multiples of 5, print "Buzz"; 
# and for multiples of both, print "FizzBuzz".

user = int(input())
for i in range(1,user+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

