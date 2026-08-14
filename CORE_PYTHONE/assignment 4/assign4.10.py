#perfect number 

Num=int(input("enter a number:"))
i = 1
sum = 0

while i < Num:
    if Num % i == 0:
        sum = sum + i
    i = i + 1

if sum == Num:
    print("Perfect number")
else:
    print("Not a perfect number")