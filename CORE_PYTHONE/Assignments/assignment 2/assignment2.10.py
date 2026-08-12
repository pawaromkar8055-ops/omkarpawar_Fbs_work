#reverse three digit number
n=int(input("enter a three digit number:"))
print(f"original number is: {n}")
r=n%10
print(f"last digit is: {r}")
m=n//10
print(f"remaining number is: {m}")
s=m%10
print(f"middle digit is: {s}")
f=m//10
print(f"first digit is: {f}")
rev=r*100+s*10+f
print(f"reversed number is: {rev}")