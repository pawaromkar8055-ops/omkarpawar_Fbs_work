#quotient and remainder of two numbers
D='Divident'
d='divisor'
D=(input('Enter the value of Divident:'))
d=(input('Enter the value of divisor:'))
Q=int(D)//int(d)
R=int(D)%int(d)
print(f"Quotient is: {Q}")
print(f"Remainder is: {R}")