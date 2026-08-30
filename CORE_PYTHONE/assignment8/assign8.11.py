n = int(input("Enter a number: "))

temp = n
sum = 0
digits = len(str(n))

for i in range(digits):
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")