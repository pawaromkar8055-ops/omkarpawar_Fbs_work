def primenum(n):
    if n > 1:
        for i in range(2, int(n/2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
n=int(input("Enter a number: "))
if primenum(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
res=primenum(n)
print("Result:", res)        