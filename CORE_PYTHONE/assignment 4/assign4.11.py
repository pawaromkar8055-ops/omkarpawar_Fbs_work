# check strong number
num = int(input("Enter number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10

    i = 1
    fact = 1

    while i <= digit:
        fact = fact * i
        i = i + 1

    sum = sum + fact
    temp = temp // 10

if sum == num:
    print("Strong number")
else:
    print("Not a strong number")