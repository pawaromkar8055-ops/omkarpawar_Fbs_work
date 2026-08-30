n = int(input("Enter a number: "))

rev = 0

for i in range(len(str(n))):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)