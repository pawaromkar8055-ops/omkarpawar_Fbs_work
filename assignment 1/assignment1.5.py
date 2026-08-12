#C.I 
P=int(input("enter amount of principle:"))
R=int(input("enter rate of interest:"))
T=int(input("enter time ( years):"))
CI = P * (1 + R/100) ** T - P
print(f"Compound Interest is: {CI}")