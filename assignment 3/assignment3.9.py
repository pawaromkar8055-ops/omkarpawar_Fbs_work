#grade
E=float(input("enter english marks:"))
M=float(input("enter maths marks:"))
H=float(input("enter hindi marks:"))
P=float(input("enter physics marks:"))
C=float(input("enter chemistry marks:"))
total=E+M+H+P+C
print(f"total marks:{total}:")
if total>=450:
    print("first class")

else:  
  print("second class")    