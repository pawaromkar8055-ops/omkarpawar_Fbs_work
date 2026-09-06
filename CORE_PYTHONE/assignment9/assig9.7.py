def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits(n // 10)
n=int(input("Enter a number: "))
res=sumofdigits(n)
print("Sum of digits of", n, "is:", res)    