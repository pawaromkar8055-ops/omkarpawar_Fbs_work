#calculate profit or loss
CS=float(input("enter cost price:"))
SP=float (input("enter selling price:"))
if SP>CS:
    print("profit is:",SP-CS)
else:
    print("loss is :",CS-SP)
    