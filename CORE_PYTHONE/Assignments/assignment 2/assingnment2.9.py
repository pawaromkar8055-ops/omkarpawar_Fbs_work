#swapping two numbers without third variable
a=10
b=20
c=a+b
a=c-a
b=c-b
print(f"after swapping a={a} and b={b}")
print(f"before swapping a={b} and b={a}")