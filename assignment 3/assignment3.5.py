#check whether triangle is equilateral , isosceles or scalene
A=float(input("enter first side:"))
a=float(input("enter first angle:"))
B=int(input("enter second side:"))
b=int(input("enter second angle"))
C=int(input('enter third side :'))
c=int(input("enter third angle:"))

if A==B and a==b and B==C and b==c:
    print("the triangle is equilateral")
else:
    print("the triangle is scalene")    

if A==B or B==C or C==A:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")    