#check all sides of triangle check whether it is valid or not
A=int(input("enter first side:"))
B=int(input("enter secound side:"))
C=int(input('enter third side:'))
if A+B>C and B+C>A and C+A>B:
    print("the triangle is valid")
else:
    print("the triangle is not valid")
    