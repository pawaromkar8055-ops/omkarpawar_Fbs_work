
def is_armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))

    for i in range(digits):
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10

    if temp == sum:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

n = int(input("Enter a number: "))     
res=is_armstrong(n)
print("Armstrong number",res)   