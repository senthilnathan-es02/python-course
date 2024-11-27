# Take the percentage as input from the user.
# Use the following conditions to assign a grade:
# 90-100: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F

mark = int(input("enter your mark : "))
if 90 <=  mark <= 100:
    print ("A grade")
elif 80 <=  mark < 89:
    print("B grade")
elif 70 <=  mark < 79:
    print("C grade")
elif  60 <= mark < 69:
    print("D grade")
elif mark < 60:
    print ("F grade")
