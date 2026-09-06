def armstrongnum(n):
    num = n
    sum = 0
    order = len(str(n))
    while num > 0:
        digit = num % 10
        sum += digit ** order
        num //= 10
    return sum == n
n=int(input("Enter a number: "))
if armstrongnum(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
res=armstrongnum(n)
print("Armstrong number",res)           