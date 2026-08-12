#cost price of book with discount percentage and selling price of book

CP=float(input("enter the cost price of book:"))
D=float(input("enter the discount percentage:"))
SP=CP-(CP*D/100)
print(f"selling price of book is: {SP}")
